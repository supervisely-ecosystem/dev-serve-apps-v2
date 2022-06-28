import json
import os

import supervisely as sly
import requests


def main():

    task_id = os.getenv("TASK_ID", None)

    if task_id is not None:
        api = sly.Api.from_env()
        response = api.task.send_request(task_id=task_id, method='/test-request/', data={})
    else:
        response = requests.post("http://127.0.0.1:8000/test-request/", data={}, timeout=1)
    print("APP returns data:")
    print(response)


if __name__ == "__main__":
    main()
