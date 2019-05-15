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
