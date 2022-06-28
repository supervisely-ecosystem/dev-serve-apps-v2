import json
import supervisely as sly
import requests


def main():
    api = sly.Api.from_env()

    api.task.send_request
    response = requests.post("http://127.0.0.1:8000/test-request/", data={}, timeout=1)
    print("APP returns data:")
    print(response)


if __name__ == "__main__":
    main()
