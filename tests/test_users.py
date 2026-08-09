from api.client import APIClient

def test_get_user():
    client = APIClient("https://jsonplaceholder.typicode.com")
    response = client.get("/users/1")
    assert response.status_code == 200

def test_create_user():
    client = APIClient("https://jsonplaceholder.typicode.com")
    data = {
        "name": "Max",
        "username": "mxsvnx",
        "email": "max@example.com"
    }
    response = client.post("/users", data)
    assert response.status_code == 201