import pytest

import challonge
import mtvmelee116

@pytest.fixture
def scraper(monkeypatch):
    monkeypatch.setattr(challonge.ChallongeScraper, 'get_raw', lambda self: mtvmelee116.raw)
    challonge_id = 'mtvmelee-mtvmelee116'
    return challonge.ChallongeScraper(challonge_id)

def test_get_matches(scraper):
    assert len(scraper.get_matches()) == 45

def test_get_players(scraper):
    assert len(scraper.get_players()) == 23

@pytest.mark.parametrize('round_name,count', [
    ('WQF', 4),
    ('WSF', 2),
    ('WF', 1),
    ('LQF', 2),
    ('LSF', 1),
    ('LF', 1),
])
def test_human_round_names(scraper, round_name, count):
    matches = scraper.get_matches()
    assert sum(1 for m in matches if m['round'] == round_name) == count
