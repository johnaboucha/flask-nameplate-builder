from flask import render_template, request, redirect, abort, flash
from application import app, db
from application.models import Nameplates
from flask_uploads import IMAGES, UploadSet, configure_uploads
from werkzeug.utils import secure_filename
from application.helpers import allowed_file
import os

app.config['UPLOADED_PHOTOS_DEST'] = "uploads"
photos = UploadSet("photos", IMAGES)
configure_uploads(app, photos)

@app.route("/nameplates/<slug>/edit")
def edit_nameplage(slug):
    nameplate = Nameplates.query.filter_by(slug=slug).first()

    if nameplate == None:
        abort(404)
    else:
        return render_template('nameplates-single-edit.html', nameplate=nameplate)

@app.route("/nameplates/<slug>")
def view_single_nameplate(slug):
    nameplate = Nameplates.query.filter_by(slug=slug).first()

    if nameplate == None:
        abort(404)
    else:
        return render_template('nameplates-single.html', nameplate=nameplate)


@app.route("/nameplates")
def view_nameplates():
    nameplates = Nameplates.query.order_by(Nameplates.date_created).all()

    return render_template('nameplates.html', nameplates=nameplates)

@app.route('/nameplates/<slug>/delete')
def delete(slug):
	nameplate_to_delete = Nameplates.query.filter_by(slug=slug).first()
	image_to_delete = nameplate_to_delete.photo

	if nameplate_to_delete == None:
		flash('Error: Nameplate not deleted. Not Found.')
		return redirect('/nameplates')

	try:
		db.session.delete(nameplate_to_delete)
		db.session.commit()
		if image_to_delete:
			if os.path.exists(app.static_folder+'/uploads/'+image_to_delete):
				os.remove(app.static_folder+'/uploads/'+image_to_delete)
		return redirect('/nameplates')
	except:
		return 'There was a problem deleting the nameplate'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	nameplate = Nameplates.query.get_or_404(id)

	if request.method == 'POST':
		nameplate.person_name = request.form['name']
		nameplate.slug = request.form['slug']
		nameplate.title = request.form['title']
		nameplate.email = request.form['email']
		nameplate.phone = request.form['phone']
		nameplate.hours = request.form['hours']
		nameplate.college = request.form['college']
		nameplate.department = request.form['department']

		try:
			if 'photo' in request.files:
				file = request.files['photo']

				if file and allowed_file(file.filename):
					filename = secure_filename(file.filename)
					filename = os.path.basename(photos.save(request.files['photo'], app.static_folder+'/uploads'))
					nameplate.photo = filename

					photos.save(request.files['photo'])
			else:
				nameplate.photo = None
			db.session.commit()
			return redirect('/nameplates/'+request.form['slug'])
		except:
			return 'There was a problem updating task'

	else:
		return redirect('/')