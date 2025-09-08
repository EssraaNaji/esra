from fastapi import APIRouter ,Depends
from src.helper.config import get_settings

app_route = APIRouter()

@app_route.get("/")
async def welcome(settings:Depends(get_settings)):

    app_name = settings.APP_NAME
    version = settings.APP_VERSION  # ✅ التعديل هنا

    return {
        app_name: version
    }
