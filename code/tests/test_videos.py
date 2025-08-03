import pytest
from httpx import AsyncClient
from services.videos.videos_service import app

@pytest.mark.asyncio
async def test_generate_video():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/generate", json={
            "prompt": "Test prompt",
            "task_id": "test-task-id",
            "subtask_id": "vid-001",
            "duration": 5,
            "fps": 24,
            "quality": "hd"
        })
        assert response.status_code == 200
        assert response.json()["result"] == "Video generated successfully"
