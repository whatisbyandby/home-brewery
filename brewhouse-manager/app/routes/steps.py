from fastapi import APIRouter, Request, status, Response
from json.decoder import JSONDecodeError
from typing import List
from app.step_controller.step_controller import Step, StepControllerError

step_router = APIRouter()


@step_router.get("/steps", status_code=200)
async def get_steps(request: Request):
    return request.app.context.get("step_controller").get_steps()


@step_router.post("/steps", status_code=200)
async def post_steps(request: Request, response: Response, steps: List[Step]):
    try:
        return request.app.context.get("step_controller").set_steps(steps)
    except (JSONDecodeError, StepControllerError) as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": str(e)}


@step_router.get("/steps/current", status_code=200)
async def get_current_step(request: Request):
    return request.app.context.get("step_controller").get_current_step()


@step_router.post("/steps/current/start", status_code=200)
async def start_current_step(request: Request):
    return request.app.context.get("step_controller").start()


@step_router.post("/steps/current/stop", status_code=200)
async def stop_current_step(request: Request):
    return request.app.context.get("step_controller").stop()


@step_router.post("/steps/next", status_code=200)
async def get_current_step(request: Request):
    return request.app.context.get("step_controller").next_step()
