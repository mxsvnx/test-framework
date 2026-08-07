from api.client import APIClient

def test_get_user():
    client = APIClient("https://jsonplaceholder.typicode.com")
    response = client.get("/users/1")
    assert response.status_code == 200
