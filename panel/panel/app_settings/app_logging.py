import os

import structlog

__all__ = ["LOGGING"]


def get_log_file_path(name: str) -> str:
    return os.path.join(os.path.dirname(__file__), f"../../../logs/{name}")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json_formatter": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(),
        },
    },
    "handlers": {
        "django": {
            "class": "logging.handlers.WatchedFileHandler",
            "filename": get_log_file_path("django.log"),
            "formatter": "json_formatter",
        },
        "root": {
            "class": "logging.handlers.WatchedFileHandler",
            "filename": get_log_file_path("root.log"),
            "formatter": "json_formatter",
        },
    },
    "loggers": {
        "django": {"handlers": ["django"], "level": "INFO"},
        "root": {"handlers": ["root"], "level": "DEBUG"},
    },
}

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso", utc=False, key="ts"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,  # noqa
    cache_logger_on_first_use=True,
)
