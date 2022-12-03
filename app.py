from flask import Flask , render_template
app = Flask(__name__)



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
   
   return render_template("signup.html")
   
@app.route("/login",methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    return render_template("logout.html")

if __name__ == "__main__":
    app.run(debug=True, port="5000")