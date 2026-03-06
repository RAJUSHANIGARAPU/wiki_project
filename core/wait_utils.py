"""
Wait Utilities

This module provides reusable utilities for handling synchronization
and timing issues in UI automation.

Web applications are asynchronous by nature, and relying only on fixed
sleep statements leads to unstable and slow tests. Centralizing wait
logic in this module helps create reliable and maintainable automation.

Typical scenarios where wait utilities are useful:

1. Waiting for elements to become visible
   Example:
       Waiting for a search results container to appear after submitting a query.

2. Waiting for elements to disappear
   Example:
       Waiting for loading spinners or overlays to disappear before interacting
       with the page.

3. Waiting for network activity to complete
   Example:
       Waiting for specific API calls or network responses triggered by UI actions.

4. Waiting for page navigation
   Example:
       Ensuring navigation is fully completed before validating page content.

5. Waiting for dynamic UI updates
   Example:
       Handling React/Vue components that update the DOM asynchronously.

6. Polling for backend-driven UI updates
   Example:
       Waiting for background processing results to appear in the UI.

7. Stabilizing flaky UI interactions
   Example:
       Retrying element interactions until the UI reaches a stable state.

8. Creating framework-level wait abstractions
   Example:
       Implementing standardized wait methods that are reused across
       page objects to avoid duplicated synchronization logic.

Although Playwright provides built-in auto-waiting mechanisms,
this module allows the framework to define additional synchronization
strategies when needed.
"""
