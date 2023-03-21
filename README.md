## FastAPI + PyTest + Asyncio Example
A small self-contained example for polling progress from an async FastAPI app. Includes tests for progress.

Run:

```bash
git clone https://github.com/tornikeo/fastapi-progress-asyncio-sample.git .
cd fastapi-progress-asyncio-sample
pip install -r requirements.txt
pytest -sxk root test_main.py
```