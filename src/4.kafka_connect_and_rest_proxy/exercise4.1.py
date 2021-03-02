import asyncio
import json
import os

import requests

KAFKA_CONNECT_URL = "http://localhost:8083/connectors"
CONNECTOR_NAME = "exercise2"

local_data_directory_filepath = os.path.join(
    os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "data"
)
docker_data_directory_filepath = "/data"


def configure_connector():
    """Calls Kafka Connect to create the Connector"""
    print("creating or updating kafka connect connector...")

    rest_method = requests.post
    resp = requests.get(f"{KAFKA_CONNECT_URL}/{CONNECTOR_NAME}")
    if resp.status_code == 200:
        return

    # See: https://docs.confluent.io/current/connect/references/restapi.html
    # See: https://docs.confluent.io/current/connect/filestream_connector.html#filesource-connector
    resp = rest_method(
        KAFKA_CONNECT_URL,
        headers={"Content-Type": "application/json"},
        data=json.dumps(
            {
                "name": CONNECTOR_NAME,
                "config": {
                    "connector.class": "FileStreamSource",
                    "topic": "lesson4.sample2.logs",
                    "tasks.max": 1,
                    "file": f"{docker_data_directory_filepath}/{CONNECTOR_NAME}.log",
                    "key.converter": "org.apache.kafka.connect.json.JsonConverter",
                    "key.converter.schemas.enable": "false",
                    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
                    "value.converter.schemas.enable": "false",
                },
            }
        ),
    )

    # Ensure a healthy response was given
    resp.raise_for_status()
    print("connector created successfully")


async def log():
    """Continually appends to the end of a file"""
    with open(f"{local_data_directory_filepath}/{CONNECTOR_NAME}.log", "w") as f:
        iteration = 0
        while True:
            f.write(f"log number {iteration}\n")
            f.flush()
            await asyncio.sleep(1.0)
            iteration += 1


async def log_task():
    """Runs the log task"""
    task = asyncio.create_task(log())
    configure_connector()
    await task


def run():
    """Runs the simulation"""
    try:
        asyncio.run(log_task())
    except KeyboardInterrupt as e:
        print("shutting down")


if __name__ == "__main__":
    run()
