from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from routes.base import  app_route
app = FastAPI()
app.include_router(app_route)