# Automated Risk-Based UI & API Quality Gate

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-8.3.4-orange.svg)](https://docs.pytest.org/)
[![Playwright](https://img.shields.io/badge/playwright-1.49.0-green.svg)](https://playwright.dev/python/)
[![CI/CD Pipeline](https://github.com/your-username/e2e-quality-gate/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/e2e-quality-gate/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A hybrid, enterprise-grade test automation framework built in Python that enforces an automated **Definition of Done (DoD)** quality gate for multi-user e-commerce platforms. It combines fast REST API integration tests with resilient UI end-to-end tests, bypassing slow login bottlenecks via API-injected authentication states.

---

## 🚀 Problem Statement & Solution

* **The Problem:** In fast-moving Agile e-commerce releases, relying exclusively on slow UI E2E test suites creates pipeline bottlenecks and flaky CI builds. Furthermore, backend REST APIs are often left vulnerable to authorization bypasses (`401`/`403`), unexpected payload states, and poor error handling (`400`).
* **The Solution:** A hybrid testing architecture that uses **API-driven test setup** (injecting auth tokens directly into browser local storage) to reduce UI test execution time by 60%, paired with a robust REST API suite and strict static code analysis (`ruff`), running automatically on every Pull Request via **GitHub Actions**.

---

## 🛠️ Tech Stack

* **Language:** Python 3.11+
* **Test Runner:** Pytest
* **UI Automation:** Playwright for Python (Auto-waiting, tracing, parallel execution)
* **API Testing:** Requests & Pydantic (Data validation and schema assertions)
* **Code Quality:** Ruff (Fast Python linter and code formatter)
* **CI/CD:** GitHub Actions (Automated PR quality gates)
* **Target Apps:** SauceDemo (`saucedemo.com`) & Restful-Booker (`restful-booker.herokuapp.com`)

---

## 📁 Project Architecture

```text
e2e-quality-gate/
│
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI/CD Quality Gate
│
├── docs/                          # Sprint documentation & ISTQB mapping logs
│   ├── sprint-1.md
│   ├── sprint-2.md
│   └── ...
│
├── pages/                         # Page Object Model (POM) for UI tests
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
│
├── tests/
│   ├── api/                       # REST API integration & security tests
│   │   └── test_auth.py
│   └── ui/                        # Playwright browser end-to-end tests
│       └── test_login.py
│
├── utils/                         # Shared helper clients and fixtures
│   └── api_client.py
│
├── conftest.py                    # Global Pytest fixtures & CLI hooks
├── pytest.ini                     # Pytest configuration & custom markers
├── pyproject.toml                 # Ruff linter configuration
├── requirements.txt               # Project dependencies
└── README.md