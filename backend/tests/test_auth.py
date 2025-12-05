import pytest
from fastapi.testclient import TestClient


@pytest.mark.asyncio
async def test_register_endpoint(client):

    # Test register success
    response = await client.post("/api/auth/register", json={"email" : "testuser@example.com", "password" : "Testpass123$"})
    assert response.status_code == 200
    assert response.json() == {"message" : "Account created."}

    # Test user exists
    response = await client.post("/api/auth/register", json={"email" : "testuser@example.com", "password" : "Testpass123$"})
    assert response.status_code == 409

@pytest.mark.asyncio
async def test_login_endpoint(client):

    await client.post("/api/auth/register", json={"email" : "testuser@example.com",  "password" : "Testpass123$"})

    # Test login sucess
    response = await client.post("/api/auth/login", json={"email" : "testuser@example.com", "password" : "Testpass123$"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()
    assert response.json()["token_type"] == "bearer"

    # Test incorrect password
    response = await client.post("/api/auth/login", json={"email" : "testuser@example.com", "password" : "wrongpass123"})
    assert response.status_code == 401

    # Test user doesn't exist
    response = await client.post("/api/auth/login", json={"email" : "nonexistent@example.com", "password" : "Testpass123$"})
    assert response.status_code == 404
