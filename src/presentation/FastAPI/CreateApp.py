from fastapi import FastAPI
from src.presentation.FastAPI.route.classify import router_classify

def CreateApp():
    app = FastAPI()


    app.include_router(router_classify)
    return app
    

