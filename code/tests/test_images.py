import pytest
from httpx import AsyncClient
from services.images.images_service import app

@pytest.mark.asyncio
async def test_generate_image():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/generate", json={
            "prompt": "Test prompt",
            "task_id": "test-task-id",
            "subtask_id": "img-001",
            "style": "photorealistic",
            "resolution": "1024x1024",
            "quality": "hd"
        })
        assert response.status_code == 200
        assert response.json()["result"] == "Image generated successfully"
