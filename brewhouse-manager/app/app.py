from fastapi import FastAPI, WebSocket, Response, status, Request, Path
from app.brewery_controller.brewery_controller import BreweryController
from app.routes.steps import step_router
from app.routes.brewhouse import brewhouse_router
from app.routes.pumps import pump_router


def create_server(context):
    app = FastAPI()

    app.brewery_controller = BreweryController(components=context)

    app.include_router(step_router)
    app.include_router(brewhouse_router)
    app.include_router(pump_router)

    @app.get("/")
    def get_home():
        return {"home_route": "Hello from the home route"}

    return app
