import pytest

from utils.api_client import APIClient

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="session")
def api_client():
    return APIClient(BASE_URL)


@pytest.fixture(scope="session")
def auth_token(api_client):
    return api_client.get_token("admin", "password123")


@pytest.fixture
def sample_booking():
    return {
        "firstname": "Alex",
        "lastname": "Berlin",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-07-01", "checkout": "2026-07-10"},
        "additionalneeds": "Dinner",
    }


@pytest.mark.api
def test_create_and_get_booking(api_client, sample_booking):
    """Verify booking creation (POST) and retrieval (GET)."""
    create_res = api_client.post("/booking", json=sample_booking)
    assert create_res.status_code == 200, f"Expected 200, got {create_res.status_code}"

    data = create_res.json()
    assert "bookingid" in data
    booking_id = data["bookingid"]

    get_res = api_client.get(f"/booking/{booking_id}")
    assert get_res.status_code == 200
    booking_data = get_res.json()
    assert booking_data["firstname"] == sample_booking["firstname"]
    assert booking_data["totalprice"] == sample_booking["totalprice"]


@pytest.mark.api
def test_update_booking_with_auth(api_client, auth_token, sample_booking):
    """Verify updating a booking (PUT) using an authenticated token header."""
    # 1. Create booking
    create_res = api_client.post("/booking", json=sample_booking)
    booking_id = create_res.json()["bookingid"]

    # 2. Update booking data
    updated_payload = sample_booking.copy()
    updated_payload["firstname"] = "Alexander"

    headers = {"Cookie": f"token={auth_token}"}
    update_res = api_client.put(
        f"/booking/{booking_id}", json=updated_payload, headers=headers
    )

    assert update_res.status_code == 200
    assert update_res.json()["firstname"] == "Alexander"


@pytest.mark.api
def test_update_booking_unauthorized(api_client, sample_booking):
    """Negative Security Test: Verify updating without token returns 403 Forbidden."""
    create_res = api_client.post("/booking", json=sample_booking)
    booking_id = create_res.json()["bookingid"]

    # Attempt update without auth cookie/token
    update_res = api_client.put(f"/booking/{booking_id}", json=sample_booking)
    assert update_res.status_code in [401, 403], (
        f"Expected 401/403, got {update_res.status_code}"
    )

@pytest.mark.api
def test_delete_booking(api_client, auth_token, sample_booking):
    """Verify deleting a booking (DELETE) with valid auth token."""
    create_res = api_client.post("/booking", json=sample_booking)
    booking_id = create_res.json()["bookingid"]

    headers = {"Cookie": f"token={auth_token}"}
    delete_res = api_client.delete(f"/booking/{booking_id}", headers=headers)
    assert delete_res.status_code in [200, 201]

    # Verify booking is gone
    get_res = api_client.get(f"/booking/{booking_id}")
    assert get_res.status_code == 404