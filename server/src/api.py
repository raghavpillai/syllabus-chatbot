from fastapi import FastAPI
from typing import Dict, Any

from src.util.response import Response

app: FastAPI = FastAPI()

API_V1_ENDPOINT = "/api/v1"

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
