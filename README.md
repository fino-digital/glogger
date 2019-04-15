# glogger

A python library for logging loguru messages straight to a gelf instance, for example Sematext via HTTP

## Install glogger

Simply install it via pip: `pip install git+https://github.com/fino-digital/glogger.git`

## Getting started
Make sure the following environment variables have been set: `ENVIRONMENT`, `LOGGING_URL` and `LOG_FACILITY`

```python
from glogger import logger

logger.info('go')
logger.bind(custom='field').info('yay')
```

