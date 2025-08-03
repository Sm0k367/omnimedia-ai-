import pytest
from httpx import AsyncClient
from services.audio.audio_service import app

@pytest.mark.asyncio
async def test_generate_audio():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/generate", json={
            "prompt": "Test prompt",
            "task_id": "test-task-id",
            "subtask_id": "audio-001",
            "audio_type": "voice",
            "voice_id": "test-voice-id"
        })
        assert response.status_code == 200
        assert response.json()["result"] == "Audio generated successfully"
