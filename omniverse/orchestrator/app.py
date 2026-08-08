import os
from datetime import datetime, timezone
from fastapi import FastAPI
from urllib.request import urlopen

app = FastAPI(title="Omniverse Orchestrator", version="0.1.0")
API_URL = os.getenv("MULTIVERSE_API_URL", "http://multiverse-api:8080")

@app.get("/health")
def health():
    api = False
    try:
        with urlopen(f"{API_URL}/health", timeout=3) as response:
            api = response.status == 200
    except Exception:
        pass
    return {
        "status": "online" if api else "degraded",
        "orchestrator": "omniverse",
        "multiverse_api": api,
        "utc": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/")
def root():
    return {"service": "omniverse-orchestrator", "dashboard": "/health"}
