import json
import httpx
import requests

BASE_URL = 'http://localhost:8000'
ENDPOINT = 'api/response'
SINGLE_URL = f"{BASE_URL}/{ENDPOINT}/single"
STREAM_URL = f"{BASE_URL}/{ENDPOINT}/stream"


class Test:

    @classmethod
    def test_single(cls, query: str) -> None:
        body: dict[str, str] = {
            "message": query
        }
        request: requests.Response = requests.get(SINGLE_URL, json=body)
        response: dict[str, str] = request.json()
        response_data: str = response.get("data")
        print(response_data)
        
    @classmethod
    def test_stream(cls, query: str) -> None:
        body: dict[str, str] = {
            "message": query
        }

        with httpx.stream('GET', STREAM_URL, json=body, timeout=None) as response:
            for chunk in response.iter_raw():
                decoded_chunk: str = chunk.decode('utf-8')
                chunk_data: dict[str, str] = json.loads(decoded_chunk)
                chunk_type: str = chunk_data.get("type")
                chunk_content: str = chunk_data.get("content")

                match chunk_type:
                    case "start":
                        print("Started response\n-------")
                    case "partial":
                        print(chunk_content, end='')
                    case "full":
                        print("\n-------\nEnded response")
                    case _:
                        print(f"Unknown: {chunk_content}")


if __name__ == "__main__":
    query: str = "What is the attendance policy?"
    Test.test_stream(query)