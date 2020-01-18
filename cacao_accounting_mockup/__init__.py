from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("/login")

@app.route("/login")
def login():
    return render_template("auth/login.html")

if __name__ == "__main__":
    app.run()