import logging
import json
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, Response, status, Request, Path
from app.brewery_controller.brewery_controller import BreweryController
from app.routes.steps import step_router
from app.routes.brewhouse import brewhouse_router
from app.routes.pumps import pump_router
from app.context import initialize_context

load_dotenv()


logging.basicConfig(filename='./log/app.log', level=logging.DEBUG, filemode='w',
                    format='%(asctime)s [%(levelname)s-%(name)s] %(message)s')


def get_config():
    with open("./config/config.json", "r") as config_file:
        return json.load(config_file)


app = FastAPI()


@app.on_event("startup")
async def startup():
    config = get_config()
    context = initialize_context(config=config)
    app.brewery_controller = BreweryController(components=context)

app.include_router(step_router)
app.include_router(brewhouse_router)
app.include_router(pump_router)


@app.get("/")
def get_home():
    return {"home_route": "Hello from the home route"}
