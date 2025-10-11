from fastapi.testclient import TestClient


def test_register_endpoint(client):

    # Test register success
    response = client.post("/api/auth/register", json={"username" : "testuser", "password" : "testpass123"})
    assert response.status_code == 200
    assert response.json() == {"message" : "Account created."}

    # Test user exists
    response = client.post("/api/auth/register", json={"username" : "testuser", "password" : "testpass123"})
    assert response.status_code == 409


def test_login_endpoint(client):

    client.post("/api/auth/register", json={"username" : "testuser",  "password" : "testpass123"})

    # Test login sucess
    response = client.post("/api/auth/login", json={"username" : "testuser", "password" : "testpass123"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()
    assert response.json()["token_type"] == "bearer"

    # Test incorrect password
    response = client.post("/api/auth/login", json={"username" : "testuser", "password" : "wrongpass123"})
    assert response.status_code == 401

    # Test user doesn't exist
    response = client.post("/api/auth/login", json={"username" : "nonexistent", "password" : "testpass123"})
    assert response.status_code == 404
