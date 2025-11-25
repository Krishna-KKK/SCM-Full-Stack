from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from routers.router import router as auth_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers.device_data import router as device_router
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
 
 
app = FastAPI()
 

BASE_DIR = Path(__file__).resolve().parent

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client.user_db
app.state.db = db

# Static Files for CSS, JS, Images
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Templates setup
templates = Jinja2Templates(directory="template")

# Routers
app.include_router(auth_router)
app.include_router(device_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
