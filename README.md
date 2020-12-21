(1) Install 'virtualenv':   
``` pip install virtualenv   ```  
(2) ```init``` virtual environment:
``` virtualenv <name> ```   
(3) Select the source:
* UNIX : ``` source <name>/bin/activate ```
* DOS : ``` .\<name>\Scripts\activate.bat```    
(4) Install 'Flask' and other packages:  
``` pip install flask flask-sqlalchemy ```   
(5) Create ```app.py```  
(6) Using Jinja2 to apply your own contents into templates. and render it using   
```python  
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    """
    docstring
    """
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug = True) 
```  
(6) Use ``` flask_sqlalchemy ``` to have an interactive communication with ur database. 
```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)
class People(db.Model):
    """
    People Table and corresponding class
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
```
(7) Deployment: 
install gunicorn 
```bash
pip install gunicorn
# freeze requirements and save 'em
pip freeze > requirements.txt
```
(8) for deploy servers such as 'huraku' you must create a `Procfile'
```procfile 

```
now u should do final commitment to the rapo and deploy!
