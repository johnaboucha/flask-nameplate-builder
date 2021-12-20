from flask import render_template, request, redirect, flash
from flask_login import login_required
from application import app, db
from application.models import Nameplates
from flask_uploads import IMAGES, UploadSet, configure_uploads
from werkzeug.utils import secure_filename
from application.forms import NameplateForm
from application.helpers import allowed_file
import os

app.config['UPLOADED_PHOTOS_DEST'] = "uploads"
photos = UploadSet("photos", IMAGES)
configure_uploads(app, photos)




@app.route("/create", methods=['GET', 'POST'])
@login_required
def create():
	form = NameplateForm()

	if request.method == 'POST' and form.validate_on_submit():
		person_name = request.form['name']
		slug = request.form['slug']
		title = request.form['title']
		email = request.form['email']
		phone = request.form['phone']
		hours = request.form['hours']
		college = request.form['college']
		department = request.form['department']

		new_nameplate = Nameplates(
			person_name=person_name,
			slug=slug,
			title=title,
			email=email,
			phone=phone,
			hours=hours,
			college=college,
			department=department,
		)

		if 'photo' in request.files:
			file = request.files['photo']

			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				filename = os.path.basename(photos.save(request.files['photo'], app.static_folder+'/uploads'))
				new_nameplate.photo = filename

		try:
			db.session.add(new_nameplate)
			db.session.commit()
			return redirect('/nameplates/'+slug)
		except Exception as e:
			flash("Error: An unkown error occured while trying to create nameplate")
			print(e)
			return redirect('/create')

	return render_template('create.html', form=form)