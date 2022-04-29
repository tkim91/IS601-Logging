import os
import json
import app.config


# def test_logfile_misc_debug():
#     """ check if misc_debug.log exists """
#     test_path = os.path.dirname(os.path.abspath(__file__))
#     log_dir = os.path.join(test_path, '../app/logs')
#     filepath = os.path.join(log_dir, "misc_debug.log")
#     assert os.path.isfile(filepath) #== False

def test_logfile_misc_debug():
    """ check if misc_debug.log exists """
    log_dir = app.config.Config.LOG_DIR
    filepath = os.path.join(log_dir, "misc_debug.log")
    assert os.path.isfile(filepath) == False


def test_logfile_request():
    test_path = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(test_path, '../app/logs')
    filepath = os.path.join(log_dir, "request.log")
    assert os.path.isfile(filepath)  # == False


def test_logfile_handler():
    test_path = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(test_path, '../app/logs')
    filepath = os.path.join(log_dir, "handler.log")
    assert os.path.isfile(filepath)


def test_logfile_myapp():
    test_path = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(test_path, '../app/logs')
    filepath = os.path.join(log_dir, "myapp.log")
    assert os.path.isfile(filepath)


def test_logfile_debug():
    test_path = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(test_path, '../app/logs')
    filepath = os.path.join(log_dir, "debug.log")
    assert os.path.isfile(filepath)


def test_logfile_error():
    test_path = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(test_path, '../app/logs')
    filepath = os.path.join(log_dir, "errors.log")
    assert os.path.isfile(filepath)


def test_logfile_sqlalchemy():
    test_path = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(test_path, '../app/logs')
    filepath = os.path.join(log_dir, "sqlalchemy.log")
    assert os.path.isfile(filepath)


def test_logfile_werkzeug():
    test_path = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(test_path, '../app/logs')
    filepath = os.path.join(log_dir, "werkzeug.log")
    assert os.path.isfile(filepath)


def test_logfile_csv():
    test_path = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(test_path, '../app/logs')
    filepath = os.path.join(log_dir, "uploads.log")
    assert os.path.isfile(filepath)
