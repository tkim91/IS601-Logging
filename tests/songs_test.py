"""This will test the song csv file upload process"""
import os
from app import db
from app.db.models import Song
from app import config
from tests.user_fixture import add_db_user_fixture # pylint: disable=unused-import


# def test_upload(application, client):
#     res = client.get("/songs/upload")
#     print(res.data)
#     assert res.status_code == 302
#     upload_res = client.post("/songs/upload", data="/sample.csv", follow_redirects=True)
#     assert upload_res.status_code == 200

