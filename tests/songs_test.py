# """This will test the song csv file upload process"""
# # pylint: disable=no-member, not-callable
#
# import csv
# import os
#
# from werkzeug.security import generate_password_hash
#
# from app import db
# from app.db.models import User, Song
#
# root = os.path.dirname(os.path.abspath(__file__))
# # set the name of the apps log folder to logs
# csvdir = os.path.join(root, '../uploads')
#
#
# def test_request_songs(client):
#     """This makes the songs page"""
#     response = client.get("/songs")
#     assert response.status_code == 200
#     assert b"Browse: Songs" in response.data
#
#
# def test_songs_upload(client, application):
#     """This will test adding songs csv files to the database"""
#     # confirm uploads folder exists
#     assert os.path.exists(csvdir) is True
#
#     # create logged in user
#     with application.app_context():
#         db.create_all()
#         user = User('test@test.com', generate_password_hash('test1234'))
#         db.session.add(user)
#         db.session.commit()
#         assert db.session.query(User).count() == 1
#         user.authenticated = True
#
#         # create a fake csv file
#         fields = ['Name', 'Artist', 'Year', 'Genre']
#         rows = [['Title 1', 'Artist 1', 'Year 1', 'Genre 1']]
#         file_name = "test-song-upload.csv"
#         file_path = os.path.join(root, '../uploads/' + file_name)
#
#         with open(file_path, 'w') as csvfile:
#             csvwriter = csv.writer(csvfile)
#             csvwriter.writerow(fields)
#             csvwriter.writerows(rows)
#
#         assert os.path.exists(file_path)
#
#         list_of_songs = []
#         with open(file_path) as file:
#             csv_file = csv.DictReader(file)
#             for row in csv_file:
#                 list_of_songs.append(Song(row['Name'], row['Artist'], row['Year'], row['Genre']))
#
#         user.songs = list_of_songs
#         db.session.commit()
#
#         test_song = Song.query.filter_by(title='Title 1').first()
#         assert test_song.title == 'Title 1'
#         assert db.session.query(Song).count() == 1
#
#         # Removes test csv
#         os.remove(file_path)
#         assert os.path.exists(file_path) is False
#
#
# def test_songs_upload_logged_in(client, application):
#     """This will test access to the songs upload page for logged in users"""
#     # create a user for the test case
#     user = User('test@test.com', generate_password_hash('test1234'))
#     #data = {'email': 'abc@test.com', 'password': 'test1234'}
#     with application.app_context():
#         db.session.add(user)
#         db.session.commit()
#         assert db.session.query(User).count() == 1
#         user.authenticated = True
#         response = client.get("/songs", follow_redirects=True)
#         assert response.status_code == 200
#         assert b"Browse: Songs" in response.data
#
#         # logged in test user can also access upload page
#         response2 = client.get("/songs/upload", follow_redirects=True)
#         assert response2.status_code == 200
#         assert b"Upload Songs" in response.data
#
#
# def test_songs_upload_denied(client):
#     """This will test access to the songs upload page for logged out users"""
#     response = client.get("/songs/upload", follow_redirects=True)
#     assert response.status_code == 200
#     assert b"Login" in response.data