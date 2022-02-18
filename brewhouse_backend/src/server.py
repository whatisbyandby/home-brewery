from urllib import response
from quart import Quart, websocket, request
import asyncio
import json
from functools import wraps

app = Quart(__name__)


@app.route("/api/set-temp", methods=['GET', 'POST'])
async def api():
    response.headers['Content-Type'] = 'application/json'
    if request.method == 'GET':
        return {"message": "Hello World"}
    if request.method == 'POST':
        return {"message": "Hello World"}


@app.route("/api/pump/<int:pump_number>", methods=['GET', 'POST'])
async def pump(pump_number):
    if request.method == 'GET':
        return json.dumps({"message": "Get Pump State"})
    if request.method == 'POST':
        return json.dumps({"message": "POST Pump State"})


connected_websockets = set()


def collect_websocket(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        global connected_websockets
        queue = asyncio.Queue()
        connected_websockets.add(queue)
        try:
            return await func(queue, *args, **kwargs)
        finally:
            connected_websockets.remove(queue)
    return wrapper


async def broadcast(message):
    for queue in connected_websockets:
        await queue.put(message)


@app.websocket("/ws")
@collect_websocket
async def ws(queue):
    while True:
        data = await queue.get()
        await websocket.send(json.dumps(data))


def initalize_server():
    return app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
