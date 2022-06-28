import supervisely as sly
from starlette.requests import Request
from supervisely import logger

import src.sly_functions as f
import src.sly_globals as g


logger.info("Application has been started")


@g.app.post('/test-request/')
def test_request(request: Request):
    logger.info("Test request received")
    print(request)
    return "Test request received"


