import logging
import os

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

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.FileHandler("reports/logs/test.log"), logging.StreamHandler()],
    )


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
    trace_path = f"reports/traces/{request.node.name}.zip"
    context.tracing.stop(path=trace_path)


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
