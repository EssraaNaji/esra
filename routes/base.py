from fastapi import FastAPI ,APIRouter
import  os

app_route = APIRouter()
@app_route.get("/")
async def welcome():

    app_name =os.getenv("APP_NAME")
    version = os.getenv("APP_VERSION")

    return {
    app_name: version
    }
