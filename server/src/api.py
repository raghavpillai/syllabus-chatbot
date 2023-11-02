from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

from src.util.response import Response
from src.model.openai_model import OpenAI

app: FastAPI = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_V1_ENDPOINT = "/api/v1"

@app.get("/")
async def default() -> Dict[str, Any]:
    res: Response = Response(
        success=True,
        message={
            "hello": "world"
        }
    )
    return res.response()
    

@app.get(f"{API_V1_ENDPOINT}/")
async def main() -> Dict[str, Any]:
    res: Response = Response(
        success=True,
        message={
            "hello2": "world2"
        }
    )
    return res.response()

@app.get(f"{API_V1_ENDPOINT}/test")
async def main(messages: list[Dict]) -> Dict[str, Any]:
    res: Response = Response(
        success=True,
        message=OpenAI.get_completion(messages)
    )
    return res.response()

@app.post(f"{API_V1_ENDPOINT}/get_response")
async def get_response(body: Dict = Body(...)) -> Dict[str, Any]:
    message: str = body.get("message")
    res: Response = Response(
        success=True,
        message=OpenAI.get_single_completion(message)
    )
    return res.response()

OpenAI.initialize()