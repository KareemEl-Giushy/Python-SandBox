# =========================
# -------------
# Config File
# -------------
# =========================
from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def indexApp():
    return render_template("index.html", mytitle="First Flask App Hamada", testy="Hello A")

@skills_app.route("/about")
def aboutApp():
    return render_template("about.html", mytitle="First Flask App Hamada", testy="Hello B")
@skills_app.route("/add")
def addApp():
    return render_template("add.html", mytitle="add From Flask")


if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)