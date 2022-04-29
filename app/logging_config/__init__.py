import logging
import os
from logging.config import dictConfig
import json
import flask
import app
from flask import request, current_app
from flask_login import current_user

#from app.logging_config.log_formatters import RequestFormatter
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
    path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(path, 'logging_config.json')
    with open(filepath, encoding="utf-8") as file:
        logging_config = json.load(file)

    add_path_to_logfile(logging_config)

    # set the name of the apps log folder to logs
    logdir = config.Config.LOG_DIR
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    logging.config.dictConfig(logging_config)

    # configure logger with JSON file
    logging.config.dictConfig(logging_config)

    # log to logfile misc_debug.log
    log = logging.getLogger("misc_debug")
    log.debug("Just configured logging")

    # log to logfile myapp.log
    log = logging.getLogger("myApp")
    log.info("Before app first request")


def add_path_to_logfile(logging_config):
    """ add logging path to logging filename """
    logdir = app.config.Config.LOG_DIR
    handlers = logging_config['handlers']
    for handler_key in handlers:
        handler = handlers[handler_key]
        if 'filename' in handler:
            log_filename = os.path.join(logdir, handler['filename'])
            logging_config['handlers'][handler_key]['filename'] = log_filename

