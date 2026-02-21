# Test Automation Framework

TestPilot is a production-grade, scalable UI automation framework built using Playwright and PyTest.
It is designed with clean architecture, CI readiness, Docker reproducibility, and recruiter-level code quality in mind.

------------------------------------------------------------------------

## Table of Contents

1.  Overview
2.  Architecture
3.  Core Features
4.  Project Structure
5.  Installation & Local Setup
6.  Running Tests
7.  Markers & Test Segmentation
8.  Docker Execution
9.  Debugging & Artifacts
10. Continuous Integration
11. Code Quality & Linting
12. Configuration & Environments
13. Design Decisions
14. Extensibility Strategy
15. License

------------------------------------------------------------------------

## 1. Overview

TestPilot is a modern UI automation framework that demonstrates:

-   Clean Page Object Model (POM)
-   JSON-based locator management
-   Plugin-based Playwright lifecycle
-   Contract-level network validation
-   Dockerized and CI-ready execution
-   Structured logging and artifact generation

The framework is built to be maintainable, scalable, and
production-ready.

------------------------------------------------------------------------

## 2. Architecture

The framework follows a layered architecture:

-   Tests → Call Flows
-   Flows → Orchestrate Pages
-   Pages → Extend BasePage
-   BasePage → Handles locator resolution
-   Locators → JSON-based configuration
-   Config → Environment-based URL management

This separation ensures clean responsibilities and maintainability.

------------------------------------------------------------------------

## 3. Core Capabilities

1.  Plugin-Based Playwright Lifecycle
2.  Multi-Browser Execution (Chromium, Firefox, WebKit)
3.  Headed and Headless Execution
4.  Parallel Execution
5.  Retry Strategy via pytest-rerunfailures
6.  Automatic Screenshot on Failure
7.  Video Recording per Test
8.  Playwright Tracing (DOM, network, timeline)
9.  Dockerized Execution
10. Mounted Artifact Persistence
11. Environment-Based Configuration
12. Structured Logging
13. GitHub Actions CI Integration
14. Artifact Upload in CI
15. Ruff Linting Enforcement
16. Pre-Commit Hook Support
17. Clean Page Object Model
18. JSON-Based Locator Strategy
19. Contract-Level Network Validation
20. Modular

------------------------------------------------------------------------

## 4. Project Structure

    project/
    ├── api/
    │   ├── clients/
    │   └── tests/
    ├── core/
    │   ├── base_page.py
    │   ├── config_reader.py
    │   └── logger.py
    ├── config/
    │   └── environments.json
    ├── ui/
    │   ├── pages/
    │   ├── flows/
    │   ├── locators/
    │   ├── testdata/
    │   └── tests/
    ├── reports/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── pytest.ini
    ├── pyproject.toml
    └── README.md

------------------------------------------------------------------------

## 5. Installation & Local Setup

### Clone Repository

    git clone <repository-url>
    cd project

### Install Dependencies

    pip install -r requirements.txt
    playwright install --with-deps

------------------------------------------------------------------------

## 6. Running Tests

Run search tests:

    pytest ui/tests/test_search.py --headed --browser chromium

Run specific browser:

    pytest ui/tests/test_search.py --browser chromium

Run headed mode:

    pytest ui/tests/test_search.py --headed --browser chromium

Run in parallel:

    pytest ui/tests/test_search.py --headed --browser chromium -n 4

------------------------------------------------------------------------

## 7. Markers & Test Segmentation

Run contract tests:

    pytest -m contract --headed --browser chromium

Run negative tests:

    pytest -m negative --headed --browser chromium

Run API tests:

    pytest -m api --headed --browser chromium

------------------------------------------------------------------------

## 8. Docker Execution

### Build Image

    docker compose build

### Run Tests

    docker compose run tests

Run with browser override:

    docker compose run tests --browser firefox

Run in parallel:

    docker compose run tests -n 4

Artifacts are persisted in the local `reports/` directory.

------------------------------------------------------------------------

## 9. Debugging & Artifacts

Open Playwright trace:

    playwright show-trace reports/traces/<trace.zip>

View recorded video:

    open reports/videos/<file>.webm

Logs are stored in:

    reports/logs/test.log

------------------------------------------------------------------------

## 10. Continuous Integration

Workflow location:

    .github/workflows/tests.yml

Pipeline includes:

-   Dependency installation
-   Playwright browser setup
-   Ruff lint check
-   Parallel test execution
-   Artifact upload

------------------------------------------------------------------------

## 11. Code Quality & Linting

Run Ruff:

    ruff check .
    ruff format .

This ensures:

-   No unused imports
-   No bare exceptions
-   Clean formatting
-   Enforced best practices

------------------------------------------------------------------------

## 12. Configuration & Environments

Environment configuration is managed via:

    config/environments.json

Switch environment using:

    pytest --env qa

The ConfigReader class dynamically resolves base URLs.

------------------------------------------------------------------------

## 13. Design Decisions

-   No raw selectors in tests
-   Centralized locator strategy
-   Flow-based test orchestration
-   Browser lifecycle managed by plugin
-   Docker-first reproducibility
-   CI integration from day one

------------------------------------------------------------------------

## 14. Extensibility Strategy

The framework supports:

-   Additional flows
-   API layer expansion
-   Cross-layer contract tests
-   Performance assertions
-   Allure report publishing
-   Multi-browser CI matrix

------------------------------------------------------------------------
