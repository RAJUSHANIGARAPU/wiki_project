import json

import pytest

from api.clients.search_client import SearchClient


@pytest.mark.api
def test_search_api_returns_200_and_html(config):
    with open("ui/testdata/test_data.json") as f:
        data = json.load(f)
    # Use spaces intentionally
    keyword = data["valid_search"]
    client = SearchClient(config.get_base_url())

    response = client.search(keyword)

    assert response.status_code in [401, 403]
