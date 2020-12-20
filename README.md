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

