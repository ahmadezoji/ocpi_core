import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import FastAPI
from app.settings import OCPI_CORE_PORT
from app.routes.locations import router
from fastapi.middleware.cors import CORSMiddleware
from app.utils.logger import Logger

app = FastAPI()
logger = Logger("ocpi_core").get_logger()

# 🔒 Add CORS middleware here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting OCPI Core API on port {OCPI_CORE_PORT}")
    uvicorn.run(app, host="0.0.0.0", port=OCPI_CORE_PORT)
