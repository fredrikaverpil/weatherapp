from loguru import logger


class ValidationError(Exception):
    def __init__(self, error_json: dict, status_code: int):
        super().__init__(error_json)

        logger.error(error_json)
        self.error_msg = error_json.get("message")
        self.status_code = status_code
