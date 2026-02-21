import json
import re

import pytest

from core.logger import logger
from ui.flows.search_flow import SearchFlow


def test_search_train(page, config):
    with open("ui/testdata/test_data.json") as f:
        data = json.load(f)

    flow = SearchFlow(page, config)

    flow.search_and_open_second_lot(data["valid_search"])

    title = flow.lot.get_title()
    favorites = flow.lot.get_favorites()
    bid = flow.lot.get_current_bid()

    print(f"Lot Name: {title}")
    print(f"Favorites: {favorites}")
    print(f"Current Bid: {bid}")

    logger.info(f"Lot Name: {title}")
    logger.info(f"Favorites: {favorites}")
    logger.info(f"Current Bid: {bid}")

    assert title != ""
    assert re.search(r"\d+", favorites)
    assert "€" in bid

@pytest.mark.negative
def test_no_results_for_empty_search(page, config):
    with open("ui/testdata/test_data.json") as f:
        data = json.load(f)
    # Use spaces intentionally
    keyword = data["empty_search"]
    flow = SearchFlow(page, config)
    flow.search_and_verify_no_results(keyword)