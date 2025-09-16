import os
from fastapi import FastAPI
from dotenv import load_dotenv


load_dotenv()

app = FastAPI(title="OCPI Core Service", version="0.1.0")

@app.get("/health", tags=["meta"])  # Simple health check
async def health():
    return {"status": "ok"}

# Include OCPI related routers
app.include_router(versions_router)

# Entrypoint for uvicorn: uvicorn ocpi_core.app.main:app --reload
