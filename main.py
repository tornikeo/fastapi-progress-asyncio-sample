import asyncio
import time
import uuid
from time import sleep

from fastapi import FastAPI

app = FastAPI()
state = {}


@app.post("/register_id")
async def register_progress_id():
    id = str(uuid.uuid4())[:8]
    state[id] = {}
    return {"id": id}


@app.get("/progress")
async def progress(id: str):
    assert id in state
    await asyncio.sleep(1)
    return {"progress": str(state[id]['progress'])}


async def long_task(loop: asyncio.AbstractEventLoop, id):
    # None uses the default executor (ThreadPoolExecutor)
    def task():
        for i in range(10):
            time.sleep(1)
            state[id]['progress'] = i / 10
    await loop.run_in_executor(None, task)
    return {"message": "Tomato"}


@app.post("/predict")
async def root(id: str):
    assert id in state
    state[id] = {'progress': 0}
    loop = asyncio.get_event_loop()
    return await long_task(loop, id)
