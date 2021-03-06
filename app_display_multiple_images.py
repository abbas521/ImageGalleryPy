import os


from flask import Flask,flash, request, render_template, send_from_directory

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        # flash("Upload Successful",'success')
        upload.save(destination)

    return render_template("complete.html", image_name=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route('/gallery')
def get_gallery():
    print(os.getcwd())
    os.chdir("D:/Python Project/upload_file_python-master/src")
    image_names = os.listdir('./images')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)

@app.route('/gallery/<filename>')
def delete_image(filename):
    os.chdir("D:/Python Project/upload_file_python-master/src/images")
    os.remove(filename)
    image_names = os.listdir()
    os.chdir("D:/Python Project/upload_file_python-master/src")
    get_gallery()
    return render_template("/gallery.html", image_names=image_names)

if __name__ == "__main__":
    app.run(port=4555, debug=True)