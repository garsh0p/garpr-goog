import flask
import logging
import os
import urlparse

import challonge

app = flask.Flask(__name__)


def url_to_id(url):
    parsed_url = urlparse.urlparse(url)
    split_netloc = parsed_url.netloc.split('.')
    if len(split_netloc) == 3 and split_netloc[0] != 'www':
        subdomain = split_netloc[0]
    else:
        subdomain = ''
    path = parsed_url.path.strip('/')

    if subdomain:
        challonge_id = subdomain + '-' + path
    else:
        challonge_id = path

    return challonge_id

@app.route('/api/upload_tournament', methods=['POST'])
def upload_tournament():
    url = flask.request.form['url']

    challonge_id = url_to_id(url)
    scraper = challonge.ChallongeScraper(challonge_id)

    print scraper.get_players()
    print scraper.get_matches()

    return flask.jsonify({
        'players': scraper.get_players(),
        'matches': scraper.get_matches()
    })


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
