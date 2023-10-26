from fastapi import FastAPI
from typing import Dict, Any
from src.util.response import Response
from src.model.openai_model import OpenAI

app: FastAPI = FastAPI()

API_V1_ENDPOINT = "/api/v1"
OPENAI_V1_ENDPOINT = "/openai/v1"

# Routes
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

@app.get(f"{OPENAI_V1_ENDPOINT}/")
async def main(messages: list[Dict]) -> Dict[str, Any]:
    res: Response = Response(
        success=True,
        message=OpenAI.get_completion(messages)
    )
    return res.response()

@app.get(f"{OPENAI_V1_ENDPOINT}/get_response")
async def get_response(message: str) -> Dict[str, Any]:
    res: Response = Response(
        success=True,
        message=OpenAI.get_single_completion(message)
    )
    return res.response()