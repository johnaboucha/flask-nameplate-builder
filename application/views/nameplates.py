from flask import render_template, request, redirect, abort, flash
from application import app, db
from application.models import Nameplates
from flask_uploads import IMAGES, UploadSet, configure_uploads
import os

photos = UploadSet("photos", IMAGES)

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
        if os.path.exists("uploads/"+image_to_delete):
            os.remove("uploads/"+image_to_delete)
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
		nameplate.photo = request.form['photo']
		nameplate.college = request.form['college']
		nameplate.department = request.form['department']

        # if 'photo' in request.files:
        #     file = request.files['photo']

        #     if file and allowed_file(file.filename):
        #         filename = secure_filename(file.filename)
        #         filename = checkDuplicateName(filename)
        #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #         nameplate.photo = secure_filename(filename)
        #     else:
        #         flash("Error: Image failed")
        #         return redirect('/update/'+str(nameplate.id))

		try:
			photos.save(request.files['photo'])
			db.session.commit()
			return redirect('/nameplates/'+request.form['slug'])
		except:
			return 'There was a problem updating task'

	else:
		return redirect('/')