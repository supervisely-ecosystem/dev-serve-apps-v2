import supervisely as sly
from fastapi import Request, FastAPI
from supervisely import logger

import src.sly_functions as f
import src.sly_globals as g


from pydantic import BaseModel, create_model


class InferenceImageIdItem(BaseModel):
    inference_image_id: int


class RequestStateItem(BaseModel):
    state: InferenceImageIdItem = None


@g.app.post('/test-request-recommended/')
async def test_request_recommended(inference_item: RequestStateItem):
    logger.info(f"{test_request_recommended.__name__} received a message")
    logger.info(f'{inference_item.state.inference_image_id=}')
    return {'status_code': 200, 'data': 'OK'}


@g.app.post('/test-request-raw/')
async def test_request_raw(request: Request):
    logger.info(f"{test_request_raw.__name__} received a message")
    # logger.info("image_id_received: %s", inference_item.inference_image_id)
    raw_body = await request.json()
    logger.info(f"{raw_body=}")

    return {'status_code': 200, 'data': 'OK'}


logger.info("Application has been started")
