import logging
import json
import asyncio
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocket, WebSocketDisconnect
from app.brewery_controller.brewery_controller import BreweryController
from app.routes.steps import step_router
from app.routes.brewhouse import brewhouse_router
from app.routes.pumps import pump_router
from app.context import initialize_context
from app.websocket.websocket import ConnectionManager


load_dotenv()


logging.basicConfig(filename='./log/app.log', level=logging.WARN, filemode='w',
                    format='%(asctime)s [%(levelname)s-%(name)s] %(message)s')


def get_config():
    with open("./config/config.json", "r") as config_file:
        return json.load(config_file)


app = FastAPI()
manager = ConnectionManager()


@app.on_event("startup")
async def startup():
    config = get_config()
    context = initialize_context(config=config)
    app.brewery_controller = BreweryController(
        components=context)
    asyncio.create_task(app.brewery_controller.run_main())


@app.on_event("shutdown")
def shutdown():
    logging.info("Shutting Down")


app.mount("/coverage", StaticFiles(directory="public"), name="coverage")

app.include_router(step_router)
app.include_router(brewhouse_router)
app.include_router(pump_router)


@app.get("/")
def get_home():
    return {"home_route": "Hello from the home route"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(1)
            data = app.brewery_controller.get_state()
            await manager.broadcast(json.dumps(data, indent=4))
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client  left the chat")
