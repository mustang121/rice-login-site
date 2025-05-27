from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 假資料帳號密碼
USERNAME = "admin"
PASSWORD = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]
        if user == USERNAME and pw == PASSWORD:
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="帳號或密碼錯誤！")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
