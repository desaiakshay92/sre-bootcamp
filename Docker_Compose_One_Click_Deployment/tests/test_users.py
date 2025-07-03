import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import status
from app.main import app

transport = ASGITransport(app=app)

@pytest.mark.asyncio
async def test_healthcheck():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/healthcheck/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "API is healthy!"}

@pytest.mark.asyncio
async def test_create_user():
    user_data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 30
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/users/", json=user_data)
    assert response.status_code == status.HTTP_200_OK
    json_response = response.json()
    assert "id" in json_response
    assert json_response["name"] == user_data["name"]
    assert json_response["email"] == user_data["email"]

@pytest.mark.asyncio
async def test_get_users():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/v1/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)