from fastapi import FastAPI
import asyncio
import time
import uuid
from time import sleep
app = FastAPI()
state = {}

@app.post('/register_id')
async def register_progress_id():
    id = str(uuid.uuid4())[:8]
    state[id] = {}
    return {'id': id}

@app.get('/progress')
async def progress(id: str):
    assert id in state
    await asyncio.sleep(1)
    return {"progress": str(time.perf_counter() - state[id])}

async def long_task(loop):
    # None uses the default executor (ThreadPoolExecutor)
    await loop.run_in_executor(None, sleep, 5)
    return {"message": "Tomato"}

@app.post("/predict")
async def root(id: str):
    assert id in state
    state[id] = time.perf_counter()
    loop = asyncio.get_event_loop()
    return await long_task(loop)