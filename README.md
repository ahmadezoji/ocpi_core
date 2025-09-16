# OCPI Core Service

A minimal FastAPI-based service skeleton for implementing OCPI (Open Charge Point Interface) endpoints.

## Features
- FastAPI application with health check endpoint at `/health`
- Placeholder OCPI versions endpoint at `/ocpi/versions`
- Environment configuration via `.env`
- Ready for extension with additional OCPI modules (Locations, Sessions, CDRs, etc.)

## Requirements
- Python 3.11+

## Setup
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# On Windows: .venv\\Scripts\\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Run (development)
```bash
uvicorn ocpi_core.app.main:app --reload --port 8000
```
Visit: http://127.0.0.1:8000/health

OCPI versions: http://127.0.0.1:8000/ocpi/versions

## Environment Variables
See `.env` for placeholders. Load order uses `python-dotenv` so ensure file exists before starting.

## Next Steps / Ideas
- Implement OCPI Version Details endpoint
- Add authentication (e.g., token-based) per OCPI spec
- Add pydantic models for each OCPI module
- Add logging configuration
- Add testing framework (pytest) and CI

## License
Internal / TBD
# ocpi_core
