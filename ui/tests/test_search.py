import logging

import pytest


@pytest.mark.smoke
def test_wikipedia_search(page, config):
    page.goto(config.get_base_url())
    search_input = page.locator("input[name='search']")
    search_input.fill("Playwright")
    search_input.press("Enter")
    logger = logging.getLogger("testpilot")
    logger.info("HELLO FROM TEST")
    assert "Playwright" in page.title()
