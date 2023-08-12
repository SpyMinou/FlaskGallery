from flask import Flask, render_template, redirect,  url_for, request, Response
from extension import db
from model import images
import os
# this is used to make the image in utf 8 after making it in base64 format
from base64 import b64encode

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///images.db"
db.init_app(app)

@app.route("/",methods=["GET", "POST"])
def index():
    list_images = images.query.all()
    # here we change all the images format, so it can be readable by the html template
    for i in list_images:
        i.image_content = b64encode(i.image_content).decode("utf-8")
    if request.method == "GET":
        return render_template("index.html",images=list_images) 
    

   
@app.route("/added",methods=["GET", "POST"])
def added():
    if request.method == "POST":
        try:
            image = request.files["image"]
            name = request.form.get("name")
            new_image = images(image_name=name,image_content=image.read())
            db.session.add(new_image)
            db.session.commit()
            print(f"Image {name} added successfully.")
            list_images = images.query.all()
            return redirect(url_for("index")) 
        except Exception as e:
            print(e)
            return(str(e))

    
@app.route("/add")
def add():
    return render_template("add.html") 

if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists("/instance/images.db"):
            db.create_all()
            print("Database created")
        else:
            print("Database already exists")
    app.run(debug=True,host="192.168.1.41")