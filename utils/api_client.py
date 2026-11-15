import requests


class APIClient:
    """Reusable API Client for RESTful Booker integration."""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json", "Accept": "application/json"})

    def get_token(self, username: str, password: str) -> str:
        """Authenticate and retrieve auth token."""
        response = self.session.post(f"{self.base_url}/auth", json={"username": username, "password": password})
        if response.status_code == 200:
            return response.json().get("token")
        raise RuntimeError(f"Failed to authenticate: {response.text}")

    def get(self, endpoint: str, headers: dict = None):
        return self.session.get(f"{self.base_url}{endpoint}", headers=headers)

    def post(self, endpoint: str, json: dict = None, headers: dict = None):
        return self.session.post(f"{self.base_url}{endpoint}", json=json, headers=headers)

    def put(self, endpoint: str, json: dict = None, headers: dict = None):
        return self.session.put(f"{self.base_url}{endpoint}", json=json, headers=headers)

    def delete(self, endpoint: str, headers: dict = None):
        return self.session.delete(f"{self.base_url}{endpoint}", headers=headers)