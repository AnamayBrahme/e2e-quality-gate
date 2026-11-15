# Sprint 3: Core CRUD REST API Integration & Negative Testing

## PART A — Clean Engineering Deliverables

### 1. Reusable API Client (`utils/api_client.py`)
Encapsulates base HTTP methods (`GET`, `POST`, `PUT`, `DELETE`), automatic header injection, and dynamic token management.

### 2. Comprehensive CRUD Test Suite (`tests/api/test_bookings.py`)
* **Create (`POST /booking`):** Generates a new dynamic booking record.
* **Read (`GET /booking/{id}`):** Validates booking schema and field values.
* **Update (`PUT /booking/{id}`):** Modifies an existing booking using an authenticated token.
* **Delete (`DELETE /booking/{id}`):** Removes a booking and verifies subsequent `404 Not Found`.

### 3. Negative & Security Validation
* Asserts `401 Unauthorized` or `403 Forbidden` when attempting to update or delete records without an auth token or with an invalid token.
* Validates boundary conditions and error handling on malformed payloads.

---

## PART B — Personal ISTQB CTFL v4.0 Study Mapping
* **Chapter 1 (Fundamentals of Testing):** Acknowledging that *exhaustive testing is impossible*, we prioritize test coverage around critical security boundaries (`401`/`403`) and data validation (`400`).
* **Chapter 2 (Testing Throughout SDLC):** API Integration testing sits at the intermediate level of the Agile Test Pyramid, validating backend contracts faster and cheaper than UI end-to-end tests.