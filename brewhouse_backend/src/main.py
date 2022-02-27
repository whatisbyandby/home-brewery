import asyncio
from brewhouse_controller import Repository, BrewhouseController
from server import initalize_server


async def main():

    repo = Repository()

    temp_controller = BrewhouseController(repo)

    app = initalize_server()

    server_task = app.run_task(host='0.0.0.0', port=5000)

    await server_task
    # await task_1


if __name__ == "__main__":
    asyncio.run(main())
