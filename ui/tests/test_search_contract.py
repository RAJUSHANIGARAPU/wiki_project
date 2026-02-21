import json

import pytest


@pytest.mark.contract
def test_search_triggers_correct_network_call(page, config):
    with open("ui/testdata/test_data.json") as f:
        data = json.load(f)

    keyword = data["valid_search"]

    page.goto(config.get_base_url())

    search_input = page.get_by_test_id("search-field").first

    with page.expect_response(f"**/s?q={keyword}") as response_info:
        search_input.fill(keyword)
        search_input.press("Enter")

    response = response_info.value

    assert response.status == 200
    assert keyword in response.url
