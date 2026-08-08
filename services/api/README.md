# Multiverse Node Registration

The API keeps a short-lived registry of connected computers/nodes in Redis.

## Register

POST `/api/v1/nodes/register`

Header: `X-API-Key: <MULTIVERSE_API_KEY>`

Body:

```json
{
  "name": "computer-01",
  "address": "192.168.1.20:8080",
  "capabilities": ["docker", "vscode"]
}
```

The service returns a generated `node_id` unless one is supplied.

## Heartbeat

POST `/api/v1/nodes/{node_id}/heartbeat`

Nodes should heartbeat before the 90-second default TTL expires. The TTL is configurable with `NODE_TTL_SECONDS`.

## List nodes

GET `/api/v1/nodes`

Header: `X-API-Key: <MULTIVERSE_API_KEY>`

Expired registrations disappear automatically from Redis.
