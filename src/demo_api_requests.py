import json
import os

import supervisely as sly
import requests


def main():
    task_id = os.getenv("TASK_ID", None)

    if task_id is not None:
        api = sly.Api.from_env()
        data = {'inference_image_id': '123'}
        # response = api.task.send_request(task_id=task_id, method='/test-request-recommended/', data=data)
        response = api.task.send_request(task_id=task_id, method='/test-request-raw/', data=data)
    else:
        data = {'state': {'inference_image_id': '123'}}
        response = requests.post("http://127.0.0.1:8000/test-request-recommended/", json=data, timeout=1)
        response = requests.post("http://127.0.0.1:8000/test-request-raw/", json=data, timeout=1)
    print("APP returns data:")
    print(response)


if __name__ == "__main__":
    main()
