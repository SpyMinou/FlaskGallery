from extension import db
class images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(100))
    image_content = db.Column(db.LargeBinary)