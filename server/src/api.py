from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from .util.response import Response
from .model.openai_model import OpenAIModel
from typing import Any

app: FastAPI = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_ENDPOINT = "/api"

@app.get("/")
async def default() -> dict[str, Any]:
    res: Response = Response(
        success=True,
        message={
            "hello": "world"
        }
    )
    return res.response()
    

@app.get(f"{API_ENDPOINT}/")
async def main() -> dict[str, Any]:
    res: Response = Response(
        success=True,
        message={
            "hello2": "world2"
        }
    )
    return res.response()

@app.get(f"{API_ENDPOINT}/response/single")
async def response(body: dict = Body(...)) -> dict[str, Any]:
    message: str = body.get("message")
    res: Response = Response(
        success=True,
        message=OpenAIModel.ask_question_single(message)
    )
    return res.response()

@app.post(f"{API_ENDPOINT}/response/stream")
async def response(body: dict = Body(...)) -> StreamingResponse:
    message: str = body.get("message")
    print(message)
    return StreamingResponse(OpenAIModel.ask_question_stream(message), media_type='text/event-stream')

OpenAIModel.initialize()