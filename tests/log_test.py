"""This tests for log file creation"""

from os.path import exists as file_exists


def test_debug_file_creation():
    assert file_exists("debug.log")


def test_request_file_creation():
    assert file_exists("request.log")
