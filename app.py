from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)
class People(db.Model):
    """
    People Table
    """
    id = db.Column(db.Integer,primary_key=True)
    firstName = db.Column(db.String(200),nullable=False)
    lastName = db.Column(db.String(200),nullable=False)
    create_date = db.Column(db.DateTime, default= datetime.utcnow)
    email = db.Column(db.String(200),nullable=False)
    def __repr__(self):
        return '<Contact %r>' %self.id
"""
    after this step, run python
    $ from app import db
    $ db.create_all()
    >> database created!
"""
@app.route('/')
def index():
    """
    docstring
    """
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug = True)