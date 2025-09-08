from fastapi import FastAPI

from src.routes.base import  app_route
app = FastAPI()
app.include_router(app_route)