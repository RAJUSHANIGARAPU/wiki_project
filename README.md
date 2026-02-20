# Playwright TestPilot Framework

Modern, scalable UI automation framework built with:

-   PyTest
-   Playwright (plugin-based lifecycle)
-   Dockerized execution
-   Parallel execution (xdist)
-   Retry strategy
-   Allure-ready reporting
-   Video and Trace recording
-   Screenshot on failure
-   Ruff linting
-   GitHub Actions CI
-   Multi-environment support

------------------------------------------------------------------------

## Overview

TestPilot is a production-ready UI automation framework designed to be:

-   Scalable
-   Maintainable
-   CI-friendly
-   Containerized
-   Architecturally clean

It leverages the official Playwright pytest plugin for modern browser
lifecycle management.

------------------------------------------------------------------------

## Architecture

project/ ├── core/ \# Core utilities (config reader, base logic) ├── ui/
│ ├── pages/ \# Page Objects │ ├── locators/ \# JSON-based locators │
├── tests/ \# Test files │ ├── fixtures/ \# UI-specific fixtures │ └──
utils/ ├── reports/ \# Logs, traces, videos, screenshots ├──
.github/workflows/ \# CI pipeline ├── docker-compose.yml ├── Dockerfile
├── pytest.ini ├── pyproject.toml \# Ruff configuration └── README.md

------------------------------------------------------------------------

## Core Capabilities

1.  Plugin-Based Playwright Lifecycle\
2.  Multi-Browser Execution (Chromium, Firefox, WebKit)\
3.  Headed and Headless Execution\
4.  Parallel Execution via pytest-xdist\
5.  Retry Strategy via pytest-rerunfailures\
6.  Automatic Screenshot on Failure\
7.  Video Recording per Test\
8.  Playwright Tracing (DOM, network, console, timeline)\
9.  Dockerized Execution\
10. Mounted Artifacts Persistence\
11. Environment-Based Configuration\
12. Structured Logging\
13. GitHub Actions CI Integration\
14. Artifact Upload in CI\
15. Ruff Linting\
16. Pre-Commit Hooks\
17. Clean Page Object Model\
18. JSON-Based Locator Strategy\
19. CI Dependency Caching\
20. Modular, Recruiter-Ready Architecture

------------------------------------------------------------------------

## Setup

### Clone Repository

git clone `<repository-url>`{=html} cd project

### Install Dependencies

pip install -r requirements.txt playwright install --with-deps

### Run Tests Locally

pytest

Run with Firefox:

pytest --browser firefox

Run in parallel:

pytest -n 4

------------------------------------------------------------------------

## Docker Usage

### Build Image

docker compose build

### Run Tests

docker compose run tests

Run with Firefox:

docker compose run tests --browser firefox

Run in parallel:

docker compose run tests -n 4

Artifacts are stored in the local reports/ directory.

------------------------------------------------------------------------

## Debugging

Open Playwright trace:

playwright show-trace reports/traces/\<trace.zip\>

View recorded video:

open reports/videos/`<file>`{=html}.webm

------------------------------------------------------------------------

## Continuous Integration

Workflow file:

.github/workflows/test.yml

Pipeline steps:

-   Install dependencies
-   Install Playwright browsers
-   Run linter
-   Execute tests in parallel
-   Upload reports as artifacts

------------------------------------------------------------------------

## Tech Stack

-   Python 3.11
-   PyTest
-   Playwright
-   Docker
-   Ruff
-   GitHub Actions

------------------------------------------------------------------------

## Future Improvements

-   Allure HTML report publishing in CI
-   Multi-browser CI matrix
-   Coverage metrics
-   Flaky test analytics
-   Template repository packaging

------------------------------------------------------------------------

## License

MIT
