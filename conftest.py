import logging
import os
import shutil
from datetime import datetime

import pytest

from core.config_reader import ConfigReader

# =========================================================
# CLI OPTIONS (ONLY ENV — let Playwright handle browser)
# =========================================================


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")


# =========================================================
# GLOBAL LOGGING SETUP
# =========================================================


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    os.makedirs("reports/logs", exist_ok=True)
    logger = logging.getLogger("wiki_project")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler("reports/logs/test.log")
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.propagate = False
    logger.info("LOGGER INITIALIZED")


# =========================================================
# ENV CONFIG FIXTURE
# =========================================================


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("env")
    return ConfigReader(env)


# =========================================================
# ENABLE VIDEO + TRACING USING PLUGIN CONTEXT
# =========================================================


@pytest.fixture(autouse=True)
def enable_artifacts(context, request):
    os.makedirs("reports/videos", exist_ok=True)
    os.makedirs("reports/traces", exist_ok=True)
    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    # Stop tracing after test
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_name = request.node.name
    browser = request.config.getoption("--browser")

    trace_path = f"reports/traces/{test_name}_{browser}_{timestamp}.zip"
    context.tracing.stop(path=trace_path)

    # Save video references before closing context
    videos = []
    for page in context.pages:
        if page.video:
            videos.append(page.video)

    context.close()

    for video in videos:
        video_path = video.path()
        new_video = f"reports/videos/{test_name}_{browser}_{timestamp}.webm"
        shutil.move(video_path, new_video)


# =========================================================
# VIDEO RECORDING CONFIG (PLUGIN WAY)
# =========================================================


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "record_video_dir": "reports/videos/"}


# =========================================================
# SCREENSHOT ON FAILURE
# =========================================================


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
