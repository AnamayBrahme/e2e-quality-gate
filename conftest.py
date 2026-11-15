def pytest_configure(config):
    """Register custom markers to avoid pytest warnings."""
    config.addinivalue_line(
        "markers", "smoke: Mark test as a critical smoke test"
    )
    config.addinivalue_line(
        "markers",
        "regression: Mark test as part of the full regression suite",
    )
    config.addinivalue_line(
        "markers", "api: Mark test as a REST API integration test"
    )
    config.addinivalue_line(
        "markers",
        "ui: Mark test as a Playwright browser automation test",
    )