# Omniverse orchestration

This directory provides the top-level launcher for the Multiverse Docker stack.

## Start everything

From the repository root:

```bash
bash omniverse/up.sh
```

Or directly:

```bash
docker compose -f omniverse/compose.yml up --build -d
```

## Stop everything

```bash
bash omniverse/down.sh
```

The orchestration layer currently starts the Multiverse API and Redis registry. Additional services can be added to `omniverse/compose.yml` as the system grows.
