import iso8601
import os
import requests
from requests_toolbelt.adapters import appengine

appengine.monkeypatch()


BASE_CHALLONGE_API_URL = 'https://api.challonge.com/v1/tournaments'
URLS = {
    'tournament': os.path.join(BASE_CHALLONGE_API_URL, '%s.json'),
    'participants': os.path.join(
            BASE_CHALLONGE_API_URL, '%s', 'participants.json'),
    'matches': os.path.join(BASE_CHALLONGE_API_URL, '%s', 'matches.json'),
}

# http://api.challonge.com/v1


class ChallongeScraper(object):
    def __init__(self, tournament_id):
        self.api_key = os.environ.get('CHALLONGE_KEY')
        self.api_key_dict = {'api_key': self.api_key}
        self.tournament_id = tournament_id

        self.raw_dict = None
        self.get_raw()

    def get_raw(self):
        if self.raw_dict is not None:
            return self.raw_dict

        self.raw_dict = {}

        for key, url in URLS.items():
            url = url % self.tournament_id
            self.raw_dict[key] = self._check_for_200(
                requests.get(url, params=self.api_key_dict)).json()

        return self.raw_dict

    def get_url(self):
        return self.get_raw()['tournament']['tournament']['full_challonge_url']

    def get_name(self):
        return self.get_raw()['tournament']['tournament']['name'].strip()

    def get_date(self):
        return iso8601.parse_date(self.get_raw()['tournament']['tournament']['created_at'])

    def _human_round_names(self, matches):
        """Convert round names from numbers into strings like WQF and LF."""
        last_round = matches[-1]['round']

        SUFFIXES = ['GF', 'F', 'SF', 'QF']

        rounds = {}
        for i, finals in enumerate(SUFFIXES):
            rounds[last_round-i] = finals
        for i, finals in enumerate(SUFFIXES[1:]):
            rounds[-(last_round-i)-1] = finals

        reset = matches[-1]['round'] == matches[-2]['round']
        reset_count = 1

        for m in matches:
            r = m['round']
            name = 'W' if r > 0 else 'L'
            if r not in rounds:
                name = '{}R{}'.format(name, abs(r))
            else:
                if rounds[r] != 'GF':
                    name += rounds[r]
                else:
                    name = 'GF'

                    if reset:
                        name += str(reset_count)
                        reset_count += 1

            m['round'] = name


    def get_matches(self):
        # sometimes challonge seems to use the "group_player_ids" parameter of "participant" instead
        # of the "id" parameter of "participant" in the "matches" api.
        # not sure exactly when this happens, but the following code checks for both
        player_map = dict()
        for p in self.get_raw()['participants']:
            if p['participant'].get('name'):
                player_name = p['participant']['name'].strip()
            else:
                player_name = p['participant'].get('username', '<unknown>').strip()
            player_map[p['participant'].get('id')] = player_name
            if p['participant'].get('group_player_ids'):
                for gpid in p['participant']['group_player_ids']:
                    player_map[gpid] = player_name

        matches = []
        for m in self.get_raw()['matches']:
            m = m['match']

            set_count = m['scores_csv']
            winner_id = m['winner_id']
            loser_id = m['loser_id']
            round_num = m['round']
            if winner_id is not None and loser_id is not None:
                winner = player_map[winner_id]
                loser = player_map[loser_id]
                # TODO db object here?
                match_result = {'winner': winner, 'loser': loser, 'round': round_num}
                matches.append(match_result)
        self._human_round_names(matches)
        return matches

    def get_players(self):
        return [p['participant']['name'].strip()
                if p['participant']['name'] else p['participant']['username'].strip()
                for p in self.get_raw()['participants']]

    def _check_for_200(self, response):
        response.raise_for_status()
        return response

