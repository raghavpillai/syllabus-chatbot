from typing import Dict, Any

class Response:
    def response(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "status_code": self.status_code,
            "data": self.message
        }

    def __init__(self,
                 success: bool,
                 message: Dict[str, Any]
                ) -> None:
        self.success: bool
        self.status_code: int
        self.message: Dict[str, Any]

        self.success = success
        self.status_code = 200 if success else 400
        self.message = message
        