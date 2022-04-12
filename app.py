from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.fullName}', '{self.username}', '{self.email}')"



@app.route("/", methods=["GET","POST"])
def home():
    return render_template("index.html")
    



@app.route("/signup", methods=["POST"])
def signup():    
    # Receives data from inputs
    fullName = request.form.get("fullName")
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    
    print(fullName, username, email, password)
    
    user = User(fullName=fullName, username=username, email=email, password=password)
    
    # Adding to the database
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("home"))
    

if __name__ == "__main__":
    app.run(debug=True)