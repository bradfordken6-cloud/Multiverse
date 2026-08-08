# Multiverse shared configuration

`multiverse.json` is the non-secret configuration shared by the API, node agents, Docker services, and VS Code tooling.

Do not put passwords, API keys, private certificates, or tokens in this file. Put secrets in `.env` or a secret manager.

The Docker network uses service names (`multiverse-api`, `redis`) for container-to-container traffic. Host applications use the published API address (`http://localhost:8080` by default).
