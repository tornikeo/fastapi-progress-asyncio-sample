import asyncio

import pytest
from httpx import AsyncClient

from main import app


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def ac():
    async with AsyncClient(app=app, base_url="http://test") as client:
        print("Client is ready")
        yield client


@pytest.mark.anyio
async def test_root(ac: AsyncClient):
    resp = await ac.post("/register_id")
    id = resp.json()["id"]
    print("Current ID", id)

    async def query_progress():
        for i in range(10):
            prog_resp = await ac.get(f"/progress", params=dict(id=id))
            assert prog_resp.status_code == 200
            print(prog_resp.json())

    async def predict():
        resp = await ac.post(f"/predict", params=dict(id=id))
        assert resp.status_code == 200
        print(resp)

    task1 = asyncio.create_task(query_progress())
    task2 = asyncio.create_task(predict())
    await asyncio.gather(task1, task2)
