from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)


class People(db.Model):
    """
    People Table and corresponding class
    """
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(200), nullable=False)
    lastName = db.Column(db.String(200), nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Contact %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        content = request.form
        print("\t >>> ADD PERSON : ", content)
        person = People(
            firstName=content['FirstName'], lastName=content['LastName'], email=content['Email'])
        try:
            db.session.add(person)
            db.session.commit()
            return redirect('/')
        except:
            return 'Ooops ... 502 BAD GATEWAY'
    else:
         people = People.query.order_by(People.create_date).all()
         return render_template('index.html', people=people)


@app.route('/delete/<int:id>')
def delete(id):
    person2del = People.query.get_or_404(id)
    try:
        db.session.delete(person2del)
        db.session.commit()
        return redirect('/')
    except:
        return 'Ooops ... 502 BAD GATEWAY'


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    person = People.query.get_or_404(id)
    if request.method == 'POST':
        data = request.form
        print("\t >>> UPDATE PERSON : ", data)
        person.firstName = data['FirstName']
        person.lastName = data['LastName']
        person.email = data['Email']
        try:
           db.session.commit()
           return redirect('/')
        except :
            return 'Ooops ... 502 BAD GATEWAY'         
       
    else:
        return render_template('update.html',person=person)

    
    

if __name__ == "__main__":
    app.run(debug = True)
