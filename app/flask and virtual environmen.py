from flask import Flask,render_template,request

app:any = Flask(__name__)

@app.route("/")
def index()->None:
    return render_template('index.html')
@app.route("/uservalidate",methods = ['POST'])
def uservalidate()->None:
    username:str = request.form['username']
    password:str = request.form['password']
    message:str = "LOGIN SUCCESS" if username == "admin" and password =="user" else"LOGIN FAILED"
    return message
    
if __name__=="__main__":
    app.run(debug=True, host'0.0.0.0')
