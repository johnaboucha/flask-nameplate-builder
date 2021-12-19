from flask import render_template, request, redirect, flash
from application import app, db
from application.models import Nameplates
from flask_uploads import IMAGES, UploadSet
from werkzeug.utils import secure_filename
from application.forms import NameplateForm

photos = UploadSet("photos", IMAGES)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/create", methods=['GET', 'POST'])
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
				#file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				new_nameplate.photo = filename

		try:
			photos.save(request.files['photo'])
			db.session.add(new_nameplate)
			db.session.commit()
			return redirect('/nameplates/'+slug)
		except:
			flash("Error: An unkown error occured while trying to create nameplate")
			return redirect('/create')

	return render_template('create.html', form=form)