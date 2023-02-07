from flask import Flask, render_template,request,flash,redirect,url_for,session
import sqlite3
from flask_mail import Mail,Message
from random import randint





app = Flask(__name__)
app.secret_key="123"
mail = Mail()

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'agyawali78@gmail.com',
    MAIL_PASSWORD = 'oiqzxkszuqsqespy'
)
mail.init_app(app)



con=sqlite3.connect("database.db")
con.execute("create table if not exists customer(sno integer primary key,firstname text,lastname text,email text unique,phone integer,password text,bio text,twitter text,facebook text,instagram text,github text,whatsapp text)")
con.close()



@app.route('/')
def index():
    session['email']="1"
    return render_template('index.html')
    
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

@app.route('/login',methods=["GET","POST"])
def login():

    if session['email']=="test":
    	if request.method=='POST':
    			    email=request.form['email']
    			    password=request.form['password']
    			    con=sqlite3.connect("database.db")
    			    con.row_factory=sqlite3.Row
    			    cur=con.cursor()
    			    cur.execute("select * from customer where email=? and password=?",(email,password))
    			    data=cur.fetchone()
    			    if data:
    			    	session['sno']=data['sno']
    			    	session['bio']=data['bio']
    			    	session['twitter']=data['bio']
    			    	session['instagram']=data['instagram']
    			    	session['facebook']=data['facebook']
    			    	session['github']=data['github']
    			    	session['whatsapp']=data['whatsapp']
    			    	session['firstname']=data['firstname']
    			    	session['lastname']=data['lastname']
    			    	session["email"]=data["email"]
    			    	session["password"]=data["password"]
    			    	return redirect("dashboard")
           			# return (session['firstname'])
    			    else:
       			     flash("Username and Password Mismatch","danger")
    else:
    	flash('You are already logged in','danger')
    	return redirect(url_for("dashboard"))
    
    
    	
       			     
	
    
    
    
    return render_template('login.html')


@app.route('/dashboard',methods=["GET","POST"])
def dashboard():
    if session['email']=='test':
    	flash("You're not logged in",'danger')
    	return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route('/signup',methods=['POST','GET'])
def signup():
     	
     	if session['email']!="test":
     		flash('Your are already logged in','danger')
     		return redirect(url_for("dashboard"))
     		
     		
     	
     	else:
     		if request.method=='POST':
     				try:
     					firstname=request.form['firstname']
     					lastname=request.form['lastname']
     					email = request.form['email']
   		  			phone=request.form['phnnbr']
     					password=request.form['password1']
   	  				cpass= request.form['password2']
     					con=sqlite3.connect("database.db")
     					cur=con.cursor()
     					if password==cpass:
     						cur.execute("insert into customer(firstname,lastname,email,phone,password)values(?,?,?,?,?)",(firstname,lastname,email,phone,password))
     						con.commit()
     						flash("Successfully Registered",'success')
     					else:
     						flash('Password amd Confirm Password do not match','danger')
     				except:
     					flash("Already registered in this email",'danger')
     	
    	 			finally:
     					con.close()
     		
     		
     	return render_template('signup.html')
    

    
    
@app.route("/edit-profile",methods=["GET","POST"])
def edit():
    if request.method=="POST":
    	try:
    		sno=session['sno']
    		bio=request.form['bio']
  	  	facebook=request.form['facebook']
 	   	instagram=request.form['instagram']
	    	twitter=request.form['twitter']
   	 	github=request.form['github']
  	  	whatsapp=request.form['whatsapp']
   	 	con=sqlite3.connect("database.db")
 	   	cur=con.cursor()
  	  	cur.execute("UPDATE customer SET  bio=?,facebook=?,instagram=?,twitter=?,github=?,whatsapp=? WHERE sno = ?;",(bio,facebook,instagram,twitter,github,whatsapp,sno))
    		con.commit()
    		session['bio']=bio
   	 	session['facebook']=facebook
    		session['instagram']=instagram
    		session['twitter']=twitter
   	 	session['github']=github
  	  	session['whatsapp']=whatsapp
  	  	flash("Successfully Updated",'success')
  	  	return redirect(url_for("dashboard"))
    	except:
    		flash('Update failed','danger')
    		
    	
    return render_template("editprofile.html")

@app.route('/logout')
def logout():
    session.clear()
    session['email']="test"
    return redirect(url_for("login"))
    
otp=randint(000000,999999)
   
@app.route('/dashboard/edit-account',methods=['GET','POST'])
def editaccount():
    if request.method=='POST':
    	editemail=request.form['email']
    	editphone=request.form['phone']
    	editpassword=request.form['password']
    	ma="Dear "+session['firstname']+" ! Your OTP from  NEG.EDU.NP"
    	
    	msg=Message("ma",
    	sender = "publicgyawali@gmail.com",
    	recipients = [session['email']]
    	)
    	msg.body=str(otp)
    	mail.send(msg)
    	session['editemail']=editemail
    	session['editphone']=editphone
    	session['editpassword']=editpassword
    	
    	
    	return redirect(url_for("validate"))
    	
    return render_template('editaccount.html')
    
   
   
   
   

    
    
@app.route('/dashboard/validate',methods=['GET','POST'])
def validate():
    if request.method=="POST":
    	otp1=request.form['otp1']
    	otp2=request.form['otp2']
    	otp3=request.form['otp3']
    	otp4=request.form['otp4']
    	otp5=request.form['otp5']
    	otp6=request.form['otp6']
    	user_otp=otp1+otp2+otp3+otp4+otp5+otp6
    	return str(user_otp)
    	if otp==int(user_otp):
    		   	try:
    	   			sno=session['sno']
    	   			editemail=session['editemail']
    			   	editphone=session['editphone']
    	 	 	 	editpassword=session['editpassword']
    			   	con=sqlite3.connect("database.db")
    		   		cur=con.cursor()
    		   		cur.execute("UPDATE customer SET  email=?,phone=?,password=? WHERE sno = ?;",(editemail,editphone,editpassword,sno))
    		   		session['email']=editemail
    	   			session['phone']=editphone
    			   	session['password']=editpassword
    		   		flash('Account Updated','success')
    			   	flash('Session expired! please re-login','danger')
    			   	session.clear()
    			   	session['email']="test"
    		   		return redirect(url_for("login"))
    		   	except:
    		   		flash('Update failed','danger')
    		   	
    		   	
    		   	
    		   
  	  	
        	#return redirect(url_for("dashboard"))
    	else:
    		#return "<h3>Please Try Again</h3>"
    		return otp
    return render_template('verify.html')
    
    
    
    
    
    
@app.route('/tester',methods=["GET","POST"])
def tester():
    if session['email']!="test":
    	return "hurray ure loggend in"
    return "sry failed"
    

if __name__ == '__main__':
    app.run(debug=True)
