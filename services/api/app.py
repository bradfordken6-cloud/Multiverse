import os
from datetime import datetime, timezone
from fastapi import FastAPI, Header, HTTPException
from redis import Redis

app = FastAPI(title="Multiverse API", version="0.1.0")
redis = Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True)
API_KEY = os.getenv("MULTIVERSE_API_KEY", "change-me")

@app.get("/health")
def health():
    redis_ok = False
    try:
        redis_ok = redis.ping()
    except Exception:
        pass
    return {"status": "ok", "service": "multiverse-api", "redis": redis_ok, "utc": datetime.now(timezone.utc).isoformat()}

@app.get("/api/v1/node")
def node(x_api_key: str | None = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return {"node": "multiverse-api", "status": "online"}
