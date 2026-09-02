# demo-app

Application FastAPI minimale utilisée comme démo pour le TP CI/CD résilient sur Kubernetes (pipeline GitHub Actions -> build/push image GHCR -> webhook signé vers un orchestrateur HA).

## Lancer en local

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Lancer les tests

```bash
pytest -v
```

## Endpoints

- `GET /` : message de bienvenue, version (`APP_VERSION`) et hostname du pod
- `GET /health` : liveness probe
- `GET /ready` : readiness probe

## Repo orchestrateur

<TODO>
