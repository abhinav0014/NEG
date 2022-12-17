from flask import Flask , render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secretkey"
db= SQLAlchemy(app)



class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50),nullable=False, unique=True)
    phone = db.Column(db.Integer(10))
    password = db.Column(db.String(20),nullable=False)
    cpassword= db.Column(db.String(20),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.firstname} - {self.email} - {self.phone}"

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/questions/BLE-Model-Questions")
def BLE():
    return render_template("BLE.html")

@app.route("/questions/SEE-Model-Questions")
def SEE():
    return render_template("SEE.html")

@app.route("/questions/12th-Boards-Model-Questions")
def XII():
    return render_template("XII.html")
    
@app.route("/oops")
def oops():
    return render_template("oops.html")

@app.route("/privacy-policy")
def pp():
    return render_template("pp.html")
    
@app.route("/signup", methods=['GET', 'POST'])
def signup():
   if request.method=='POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phnnbr']
        password = request.form['password1']
        cpassword = request.form['password2']
        user = User(firstname=firstname,lastname=lastname,email=email,phone=phone,password=password)
        if password == cpassword:
        	db.session.add(user)
        	db.session.commit()
        	else:
        	flash('Password and Confirm Password do not match!')
        	
        
   return render_template("signup.html")
   
@app.route("/login",methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        
    return render_template('login.html')

@app.route("/logout")
def logout():
    return render_template("logout.html")

if __name__ == "__main__":
    app.run(debug=True, port="5000")