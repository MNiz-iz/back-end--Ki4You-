import uvicorn
from fastapi import FastAPI
from app.config import db


def init_app():
    db.init()

    app = FastAPI(
        title="Ki4You web-application",
        description="WEB Application for plants recommendation by user requirement",
        version="1"
    )

    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    from app.controller import tree_data, recommend
    from fastapi.middleware.cors import CORSMiddleware

    app.add_middleware(
        CORSMiddleware,
        #url for allow crosite
        allow_origins=["http://127.0.0.1:5500"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(tree_data.router)
    #app.include_router(recommend.router)

    app.include_router(
        recommend.router,
        prefix="/form",
        tags=["form"]
    )

    return app


app = init_app()


def start():
    #url for start api
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)