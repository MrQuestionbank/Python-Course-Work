from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class Todo(db.model):
    id = db.column(db.Integer, primary_key = True)
    title = db.column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route("/")
def index():
    return render_template("base.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
