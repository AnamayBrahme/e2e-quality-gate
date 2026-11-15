# 🚀 Hybrid Test Automation & Quality Gate Framework

[![CI/CD Quality Gate](https://github.com/AnamayBrahme/e2e-quality-gate/actions/workflows/ci.yml/badge.svg)](https://github.com/AnamayBrahme/e2e-quality-gate/actions/workflows/ci.yml)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-8.x-orange.svg)](https://docs.pytest.org/)
[![Playwright](https://img.shields.io/badge/playwright-1.x-green.svg)](https://playwright.dev/python/)
[![Ruff](https://img.shields.io/badge/linter-ruff-red.svg)](https://github.com/astral-sh/ruff)
[![ISTQB CTFL v4.0](https://img.shields.io/badge/ISTQB-CTFL_v4.0_Aligned-purple.svg)](https://www.istqb.org/)

A production-grade, portfolio-ready hybrid **UI + API Test Automation Framework** engineered with Python, Pytest, Playwright, Requests, and GitHub Actions. Built following rigorous Agile Scrum delivery principles (6 Sprints) and aligned with ISTQB CTFL v4.0 software testing standards.

---

## 🏗️ Architecture & Tech Stack

```text
e2e-quality-gate/
├── .github/workflows/ci.yml   # Automated GitHub Actions CI pipeline
├── pages/                     # Playwright Page Object Model (POM) classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                     # Test Suites (API & UI)
│   ├── api/                   # RESTful Booker API & CRUD tests
│   └── ui/                    # SauceDemo UI & E2E Checkout flows
├── utils/                     # Reusable API Client wrappers
├── docs/                      # Agile Sprints 1-6 Documentation & Risk Matrices
├── requirements.txt           # Pinned dependencies
├── pytest.ini                 # Global pytest configuration & markers
└── .gitignore                 # Enterprise-grade exclusions


## 🛠️ Target Applications Tested
1. **UI Automation:** **SauceDemo** ([https://www.saucedemo.com](https://www.saucedemo.com)) — Modern mock e-commerce web application.
2. **API Automation:** **Restful Booker** ([https://restful-booker.herokuapp.com](https://restful-booker.herokuapp.com)) — Sandbox REST API for backend validation.

---

## ⚡ Quickstart Guide

### 1. Clone & Setup Environment
```bash
git clone [https://github.com/AnamayBrahme/e2e-quality-gate.git](https://github.com/AnamayBrahme/e2e-quality-gate.git)
cd e2e-quality-gate

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

pip install -r requirements.txt
playwright install chromium

### 2. Run Quality Checks & Tests
```bash
# Run linting check
ruff check .

# Run API tests
pytest -m api -v

# Run UI tests
pytest -m ui -v