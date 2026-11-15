# Sprint 2: Risk Analysis, Test Design & Authentication API Suite

## PART A — Clean Engineering Deliverables

### 1. Product Risk Matrix (`Risk = Likelihood × Impact`)
| Feature / Endpoint | Risk Description | Likelihood (1-3) | Impact (1-3) | Risk Score | Mitigation Strategy |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `POST /auth` (Valid Login) | Authentication token fails to generate for valid credentials. | 1 | 3 | **3 (Low)** | Automated smoke test validating `200 OK` and token string presence. |
| `POST /auth` (Invalid Credentials) | Unauthorized users gain access or system returns `500` instead of `400`/`401`. | 2 | 3 | **6 (Medium)** | Negative testing suite asserting clean error response handling. |
| `POST /auth` (Missing Payload Fields) | API crashes or throws unhandled exception when required parameters are omitted. | 2 | 2 | **4 (Medium)** | Boundary value and negative schema assertion tests. |

### 2. Black-Box Test Design Specifications
* **Technique 1: Equivalence Partitioning (EP)**
  * *Valid Partition:* Correct username (`admin`) and correct password (`password123`) $\rightarrow$ Expected: `200 OK` with session token.
  * *Invalid Partition:* Incorrect username or incorrect password $\rightarrow$ Expected: Failure message (`Bad credentials`).
* **Technique 2: Boundary Value Analysis (BVA)**
  * *Empty Payload:* `{"username": "", "password": ""}` $\rightarrow$ Expected: Handled gracefully without server crash.
  * *Missing Key:* Omitting the password key entirely $\rightarrow$ Expected: Client/Server rejection status.

### 3. Automated Authentication API Suite
Implemented `tests/api/test_auth.py` covering positive token generation and negative boundary checks.