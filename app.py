import os
import secrets
from static.python.img_process import process_img
from flask import Flask, request, redirect, render_template, flash

UPLOAD_FOLDER = ("static/uploads")
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
app.config["SECRET_KEY"] = secrets.token_urlsafe(32)



@app.route("/")
def upload_form():
    return render_template("index.html", OUTPUT="EXTENSION NOT ALLOWED")

# upload the images and save


@app.route("/upload", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            img = request.files["uploads"]
            quality = int(request.form["quality"])
            
            filename, file_extension = os.path.splitext(img.filename)
            if file_extension not in ALLOWED_EXTENSIONS:
                flash("Invalid file extension.")
                return redirect("/")
            path = os.path.join(app.config["UPLOAD_FOLDER"], f"input{file_extension}")
            img.save(path)
            process_img(path, file_extension, quality)
            return redirect("/")
            
@app.route("/download")
def download_image():
    
    
    return



@app.route("/imageview")
def image_view():
    return render_template("image_view.html", result="static/output/test.jpg")


# run the flask server
if __name__ == "__main__":
    app.run(debug=True)

