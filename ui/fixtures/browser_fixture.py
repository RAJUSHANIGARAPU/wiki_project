import os

import pytest
from playwright.sync_api import sync_playwright

from core.config_reader import ConfigReader


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(playwright_instance, request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless") == "true"

    browser = getattr(playwright_instance, browser_name).launch(headless=headless)

    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser, request):
    os.makedirs("reports/videos", exist_ok=True)
    os.makedirs("reports/traces", exist_ok=True)

    context = browser.new_context(record_video_dir="reports/videos")

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    yield page

    context.tracing.stop(path=f"reports/traces/{request.node.name}.zip")

    context.close()


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    return ConfigReader(env)
