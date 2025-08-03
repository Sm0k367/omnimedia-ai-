import pytest
from httpx import AsyncClient
from services.orchestrator.orchestrator import app

@pytest.mark.asyncio
async def test_generate_media():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/generate-media", json={
            "prompt": "Test prompt",
            "output_format": "mixed/package",
            "options": {
                "style": ["cinematic"],
                "quality": ["ultra-hd"],
                "policy": ["unrestricted"]
            }
        })
        assert response.status_code == 200
        assert "task_id" in response.json()

@pytest.mark.asyncio
async def test_task_status():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/task-status/test-task-id")
        assert response.status_code == 404
