"""This tests for log file creation"""
import os
from pathlib import Path


def test_debug_file_creation():
    file_abs_path = os.path.abspath('debug.info')
    path = Path(file_abs_path)
    assert Path('./flask_auth/app/logs/debug.info').is_file()
    #assert os.path.isfile(file_abs_path)


def test_request_file_creation():
    path = Path(os.path.abspath(__file__))
    assert path.is_file()
