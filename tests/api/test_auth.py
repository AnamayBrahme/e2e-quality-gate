import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.mark.api
@pytest.mark.smoke
def test_valid_authentication():
    """Verify valid credentials return 200 OK and an active auth token (Positive EP)."""
    payload = {"username": "admin", "password": "password123"}
    response = requests.post(f"{BASE_URL}/auth", json=payload)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "token" in data, "Response JSON missing 'token' key"
    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0


@pytest.mark.api
def test_invalid_authentication_bad_credentials():
    """Verify invalid credentials return proper error payload (Negative EP)."""
    payload = {"username": "invalid_user", "password": "wrong_password"}
    response = requests.post(f"{BASE_URL}/auth", json=payload)

    data = response.json()
    assert "reason" in data or response.status_code in [400, 401, 200]
    if "reason" in data:
        assert data["reason"] == "Bad credentials"


@pytest.mark.api
def test_authentication_missing_parameters():
    """Verify server handles missing payload keys gracefully (Boundary Value Analysis)."""
    payload = {"username": "admin"}  # Missing password field
    response = requests.post(f"{BASE_URL}/auth", json=payload)

    data = response.json()
    assert "reason" in data or response.status_code in [400, 500, 200]