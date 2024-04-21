import sys
import logging
from loguru import logger


logger.remove()

logger.add(
    sys.stderr,
    format="<green>[{time:YYYY-MM-DD HH:mm:ss}]</green> <level> {level} </level> <level><white> {message} </white></level>",
    level="TRACE",
    enqueue=True,
    backtrace=True,
    diagnose=True,
    colorize=True,
)

logger.add(
    "logs/log_trace_{time:YYYY-MM-DD}.log",
    rotation="00:00",
    retention="10 days",
    format="[ {time:YYYY-MM-DD HH:mm:ss} ] [ {level} ] {message}",
    level="TRACE",
    enqueue=True,
    backtrace=True,
    diagnose=True,
)

logger.add(
    "logs/log_error_{time:YYYY-MM-DD}.log",
    rotation="00:00",
    retention="10 days",
    format="[ {time:YYYY-MM-DD HH:mm:ss} ] [ {level} ] {message}",
    level="ERROR",
    enqueue=True,
    backtrace=True,
    diagnose=True,
)

logger.level("DEBUG", color="<cyan>")
logger.level("INFO", color="<green>")
logger.level("WARNING", color="<yellow>")
logger.level("ERROR", color="<red>")
logger.level("CRITICAL", color="<magenta>")


class InterceptHandler(logging.Handler):
    def emit(self, record):
        loguru_logger = logger.bind(request_id="some_request_id")
        loguru_logger.log(record.levelno, record.getMessage())


intercept_handler = InterceptHandler()

logging.getLogger("uvicorn.access").handlers = [intercept_handler]
