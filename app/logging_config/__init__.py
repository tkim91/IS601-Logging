import logging
import os
from logging.config import dictConfig
import json
import flask
import app
from flask import request, current_app
from flask_login import current_user

# from app.logging_config.log_formatters import RequestFormatter
from app import config

log_con = flask.Blueprint('log_con', __name__)


@log_con.before_app_request
def before_request_logging():
    current_app.logger.info("Before request")
    log = logging.getLogger("myApp")
    log.info("My App Logger")


@log_con.after_app_request
def after_request_logging(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    elif request.path.startswith('/bootstrap'):
        return response
    current_app.logger.info("After Request")

    # logging requests
    log = logging.getLogger("request")
    log.info('Response status: ' + response.status)
    # logging to debug
    log = logging.getLogger("myApp")
    log.debug("My App Logger")
    return response


@log_con.before_app_first_request
def setup_logs():
    # path = os.path.dirname(os.path.abspath(__file__))
    # filepath = os.path.join(path, 'logging_config.json')
    # with open(filepath, encoding="utf-8") as file:
    #     logging_config = json.load(file)
    #
    # add_path_to_logfile(logging_config)

    # set the name of the apps log folder to logs
    logdir = config.Config.LOG_DIR
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    logging.config.dictConfig(LOGGING_CONFIG)


def add_path_to_logfile(logging_config):
    """ add logging path to logging filename """
    logdir = app.config.Config.LOG_DIR
    handlers = logging_config['handlers']
    for handler_key in handlers:
        handler = handlers[handler_key]
        if 'filename' in handler:
            log_filename = os.path.join(logdir, handler['filename'])
            logging_config['handlers'][handler_key]['filename'] = log_filename


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
        "RequestFormatter": {
            "()": "app.logging_config.log_formatters.RequestFormatter",
            "format": "[%(asctime)s] [%(process)d] %(remote_addr)s requested %(url)s %(levelname)s in %(module)s: %(message)s"
        }
    },
    "handlers": {
        "default": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout"
        },
        "file.handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": "logs/flask.log",
            "maxBytes": 10000000,
            "backupCount": 5
        },
        "file.handler.myapp": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": "logs/myapp.log",
            "maxBytes": 10000000,
            "backupCount": 5
        },
        "file.handler.request": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "RequestFormatter",
            "filename": "logs/request.log",
            "maxBytes": 10000000,
            "backupCount": 5
        },
        "file.handler.errors": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": "logs/errors.log",
            "maxBytes": 10000000,
            "backupCount": 5
        },
        "file.handler.sqlalchemy": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": "logs/sqlalchemy.log",
            "maxBytes": 10000000,
            "backupCount": 5
        },
        "file.handler.werkzeug": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": "logs/werkzeug.log",
            "maxBytes": 10000000,
            "backupCount": 5
        },
        "file.handler.misc_debug": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": "logs/misc_debug.log",
            "maxBytes": 10000000,
            "backupCount": 5
        },
        "file.handler.csv": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": "logs/uploads.log",
            "maxBytes": 10000000,
            "backupCount": 5
        }
    },
    "loggers": {
        "": {
            "handlers": ["default", "file.handler"],
            "level": "DEBUG",
            "propagate": True
        },
        "__main__": {
            "handlers": ["default", "file.handler"],
            "level": "DEBUG",
            "propagate": True
        },
        "werkzeug": {
            "handlers": ["file.handler.werkzeug"],
            "level": "DEBUG",
            "propagate": False
        },
        "sqlalchemy.engine": {
            "handlers": ["file.handler.sqlalchemy"],
            "level": "INFO",
            "propagate": False
        },
        "myApp": {
            "handlers": ["file.handler.myapp"],
            "level": "DEBUG",
            "propagate": False
        },
        "myerrors": {
            "handlers": ["file.handler.errors"],
            "level": "DEBUG",
            "propagate": False
        },
        "misc_debug": {
            "handlers": ["file.handler.misc_debug"],
            "level": "DEBUG",
            "propagate": False
        },
        "request": {
            "handlers": ["file.handler.request"],
            "level": "INFO",
            "propagate": False
        },
        "csv": {
            "handlers": ["file.handler.csv"],
            "level": "DEBUG",
            "propagate": False
        }
    }
}
