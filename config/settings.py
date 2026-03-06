"""
Global Framework Settings

This module is reserved for framework-wide configuration and constants that are
independent of environment-specific settings.

Environment variables such as base URLs or credentials are stored in
`environments.json` and loaded via `ConfigReader`. This file instead holds
global settings that control how the automation framework behaves.

Keeping these values centralized improves maintainability, readability,
and prevents "magic numbers" or scattered configuration across the codebase.

Typical scenarios where this module would be used:

1. Global framework constants
   Example:
       DEFAULT_TIMEOUT = 10000
       RETRY_COUNT = 2
       SCREENSHOT_ON_FAILURE = True

2. Default Playwright browser configuration
   Example:
       BROWSER = "chromium"
       HEADLESS = True
       VIEWPORT = {"width": 1280, "height": 720}
       TRACE_ENABLED = True
       VIDEO_RECORDING = True

3. Feature flags for tests
   Allows enabling/disabling certain test layers.
   Example:
       ENABLE_UI_TESTS = True
       ENABLE_API_TESTS = True
       ENABLE_CONTRACT_TESTS = True

4. Retry and stability configuration
   Example:
       MAX_RETRIES = 2
       RETRY_DELAY_SECONDS = 3

5. UI wait and timeout configuration
   Example:
       ELEMENT_TIMEOUT = 5000
       PAGE_LOAD_TIMEOUT = 20000
       NETWORK_IDLE_TIMEOUT = 10000

6. CI vs local execution behavior
   Example:
       IS_CI = os.getenv("CI") == "true"

   This allows the framework to change behavior depending on the runtime
   environment (for example enabling video recording only in CI).

7. Framework paths
   Example:
       TESTDATA_DIR = "ui/testdata"
       LOCATORS_DIR = "ui/locators"
       REPORT_DIR = "reports"

8. Framework metadata
   Example:
       FRAMEWORK_NAME = "Wiki Playwright Automation"
       FRAMEWORK_VERSION = "1.0"

Currently this module is intentionally minimal but exists as an extension
point for future framework configuration as the project grows.
"""
