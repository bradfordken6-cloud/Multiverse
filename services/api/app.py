import json
import os
import uuid
from datetime import datetime, timezone

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field
from redis import Redis

app = FastAPI(title="Multiverse API", version="0.2.0")
redis = Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True)
API_KEY = os.getenv("MULTIVERSE_API_KEY", "change-me")
NODE_TTL_SECONDS = int(os.getenv("NODE_TTL_SECONDS", "90"))
NODE_PREFIX = "multiverse:node:"


class NodeRegistration(BaseModel):
    node_id: str | None = None
    name: str = Field(min_length=1, max_length=100)
    address: str = Field(min_length=1, max_length=255)
    capabilities: list[str] = Field(default_factory=list)


def require_key(x_api_key: str | None):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")


def now():
    return datetime.now(timezone.utc).isoformat()


@app.get("/health")
def health():
    redis_ok = False
    try:
        redis_ok = redis.ping()
    except Exception:
        pass
    return {"status": "ok", "service": "multiverse-api", "redis": redis_ok, "utc": now()}


@app.get("/api/v1/node")
def node(x_api_key: str | None = Header(default=None)):
    require_key(x_api_key)
    return {"node": "multiverse-api", "status": "online"}


@app.post("/api/v1/nodes/register")
def register_node(payload: NodeRegistration, x_api_key: str | None = Header(default=None)):
    require_key(x_api_key)
    node_id = payload.node_id or str(uuid.uuid4())
    record = {
        "node_id": node_id,
        "name": payload.name,
        "address": payload.address,
        "capabilities": payload.capabilities,
        "status": "online",
        "last_seen": now(),
    }
    redis.setex(f"{NODE_PREFIX}{node_id}", NODE_TTL_SECONDS, json.dumps(record))
    return record


@app.post("/api/v1/nodes/{node_id}/heartbeat")
def heartbeat(node_id: str, x_api_key: str | None = Header(default=None)):
    require_key(x_api_key)
    key = f"{NODE_PREFIX}{node_id}"
    raw = redis.get(key)
    if not raw:
        raise HTTPException(status_code=404, detail="Node not registered")
    record = json.loads(raw)
    record["status"] = "online"
    record["last_seen"] = now()
    redis.setex(key, NODE_TTL_SECONDS, json.dumps(record))
    return record


@app.get("/api/v1/nodes")
def list_nodes(x_api_key: str | None = Header(default=None)):
    require_key(x_api_key)
    nodes = []
    for key in redis.scan_iter(match=f"{NODE_PREFIX}*"):
        raw = redis.get(key)
        if raw:
            nodes.append(json.loads(raw))
    return {"count": len(nodes), "nodes": nodes}
