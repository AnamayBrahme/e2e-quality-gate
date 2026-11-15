# Sprint 5: Hybrid End-to-End Checkout Flow & Defect Management

## PART A — Clean Engineering Deliverables

### 1. Page Objects (`CartPage`, `CheckoutPage`)
* **`CartPage` (`pages/cart_page.py`):** Handles cart item validation and proceeding to checkout.
* **`CheckoutPage` (`pages/checkout_page.py`):** Handles customer details form input (`First Name`, `Last Name`, `Postal Code`), order overview confirmation, and success header validation (`Thank you for your order!`).

### 2. Exploratory Testing Session Log
* **Session Focus:** SauceDemo checkout form boundary handling.
* **Edge Case Explored:** Entering special characters and SQL/XSS injection payloads in postal code fields.
* **Observation:** Input fields correctly sanitize or restrict non-alphanumeric values, ensuring robust form handling.

### 3. Defect Report Template
* **Defect ID:** DEF-001
* **Title:** Total price calculation omits dynamic regional tax in cart overview.
* **Severity / Priority:** Medium / Medium
* **Steps to Reproduce:** Add items totaling $29.99 to cart, navigate to checkout step two, inspect price summary.
* **Expected Result:** Item total plus tax equals final total.
* **Actual Result:** Tax displays as `$0.00` in sandbox mode.
* **Evidence:** Playwright trace recording attached.

---

## PART B — Personal ISTQB CTFL v4.0 Study Mapping
* **Chapter 1 (Fundamentals of Testing):** Distinguishing **Error** (developer oversight), **Defect** (fault in code), and **Failure** (incorrect output) via Root Cause Analysis.
* **Chapter 2 (Test Types):** Combining **E2E Integration Testing** (automated journey) with **Exploratory Testing** (human error-guessing).