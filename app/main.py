import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import FastAPI
from app.settings import OCPI_CORE_PORT
from app.routes.locations import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
    uvicorn.run(app, host="0.0.0.0", port=OCPI_CORE_PORT)
