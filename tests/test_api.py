import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users_status_code():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200


def test_get_users_returns_json():
    response = requests.get(f"{BASE_URL}/users")

    assert response.headers["Content-Type"].startswith("application/json")


def test_get_users_returns_data():
    response = requests.get(f"{BASE_URL}/users")

    data = response.json()

    assert len(data) > 0


def test_user_contains_required_fields():
    response = requests.get(f"{BASE_URL}/users")

    data = response.json()

    user = data[0]

    assert "id" in user
    assert "name" in user
    assert "email" in user