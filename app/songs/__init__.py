import csv
import logging
import os

from flask import Blueprint, render_template, abort, url_for,current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.db import db
from app.db.models import Song
from app.songs.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

songs = Blueprint('songs', __name__,
                        template_folder='templates')

@songs.route('/songs', methods=['GET'], defaults={"page": 1})
@songs.route('/songs/<int:page>', methods=['GET'])
def songs_browse(page):
    page = page
    per_page = 1000
    pagination = Song.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        current_app.logger.info(str(current_user.get_id()) + " accessed browse songs page")
        return render_template('browse_songs.html',data=data,pagination=pagination)
    except TemplateNotFound:
        current_app.logger.info(current_user.get_id() + " cannot access browse songs page - 404")
        abort(404)

@songs.route('/songs/upload', methods=['POST', 'GET'])
@login_required
def songs_upload():
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("csv")

        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)

        #user = current_user
        list_of_songs = []
        with open(filepath, encoding="utf-8") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_of_songs.append(Song(row['Name'],row['Artist'],row['Year'],row['Genre']))

        current_user.songs = list_of_songs
        db.session.commit()
        log.info(filename + " upload by: " + current_user.email)
        return redirect(url_for('auth.dashboard'))
    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)