import pytest
from httpx import AsyncClient
from services.text.text_service import app

@pytest.mark.asyncio
async def test_generate_text():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/generate", json={
            "prompt": "Test prompt",
            "task_id": "test-task-id",
            "subtask_id": "text-001",
            "max_tokens": 100,
            "temperature": 0.7
        })
        assert response.status_code == 200
        assert response.json()["result"] == "Text generated successfully"
