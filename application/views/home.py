from flask import render_template, redirect, flash, send_from_directory
from application import app

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.errorhandler(413)
def file_too_big(e):
    flash('Error: The image was too large. Size limit is 2MB.')
    return redirect('/create')