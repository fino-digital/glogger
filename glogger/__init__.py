import json
import os
import threading

import requests
from loguru import logger

LOGGING_URL = os.getenv("LOGGING_URL", "") + "glogger"
s = requests.Session()


def send_as_gelf(record):
    k = json.loads(record)
    data = {
        "message": k["record"]["message"],
        "severity": k["record"]["level"]["name"],
        "level": k["record"]["level"]["no"],
        "thread": k["record"]["thread"]["name"],
        "timestamp": k["record"]["time"]["timestamp"],
        "source_name": k["record"]["file"]["path"] + ":" + k["record"]["module"],
        "source_line_number": k["record"]["line"],
        "source_method_name": k["record"]["function"],
    }
    for k, v in k["record"]["extra"].items():
        data[k] = v

    s.post(LOGGING_URL, json=data)


class Gelf:
    def write(self, record):
        if "LOGGING_URL" not in os.environ:
            return
        t = threading.Thread(target=send_as_gelf, args=[record])
        t.daemon = True
        t.start()


logger.add(sink=Gelf(), serialize=True)

if "ENVIRONMENT" in os.environ:
    logger = logger.bind(environment=os.getenv("ENVIRONMENT"))
else:
    logger.warning("ENVIRONMENT not configured")

if "LOG_FACILITY" in os.environ:
    logger = logger.bind(facility=os.getenv("LOG_FACILITY"))
else:
    logger.warning("LOG_FACILITY not configured")
