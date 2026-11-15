# Sprint 4: UI Test Automation Foundation with Page Object Model (POM)

## PART A — Clean Engineering Deliverables

### 1. Page Object Model (POM) Architecture
* **`BasePage` (`pages/base_page.py`):** Encapsulates core browser navigation, element selectors, and Playwright auto-waiting assertions.
* **`LoginPage` (`pages/login_page.py`):** Encapsulates username input, password input, login button action, and error message retrieval.
* **`InventoryPage` (`pages/inventory_page.py`):** Encapsulates product catalog header assertions and inventory display verification.

### 2. UI Test Suite (`tests/ui/test_login.py`)
* **Standard User Login:** Verifies successful navigation and redirection to the inventory page (`/inventory.html`).
* **Locked Out User:** Verifies that entering locked-out credentials displays the correct error banner (`Epic sadface: Sorry, this user has been locked out`).

---

## PART B — Personal ISTQB CTFL v4.0 Study Mapping
* **Chapter 4 (Test Analysis & Design):** Applying **State Transition Testing** to model the user authentication flow (Logged-Out $\rightarrow$ Authenticated / Locked-Out).
* **Chapter 6 (Test Tools):** Leveraging Playwright's built-in auto-waiting mechanisms and trace capture capabilities to eliminate test flakiness caused by asynchronous network loading.