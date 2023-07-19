from backend.routers.base import api_router
from backend.apps.base import app_router
from backend.core.config import Settings
from backend.db.base import Base
from backend.db.session import engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def include_router(app):
    app.include_router(api_router)
    #app.include_router(app_router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def configure_staticfiles(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
   # configure_staticfiles(app)
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}