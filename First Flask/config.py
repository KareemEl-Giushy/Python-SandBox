# =========================
# -------------
# Config File
# -------------
# =========================
from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def indexApp():
    return render_template("index.html", mytitle="First Flask App Hamada")

@skills_app.route("/about")
def aboutApp():
    return render_template("about.html", mytitle="First Flask App Hamada")
@skills_app.route("/add")
def addApp():
    return render_template("add.html", mytitle="add From Flask", cssfiles=['add.css'])

@skills_app.route("/skills")
def skills():
    return render_template("skills.html",
                            mytitle="My Skills",
                            page_head="These are my skills",
                            discription="This is my skills page", cssfiles=['skills.css'], skills=[("html", 90), ("css", 90), ('php', 80), ('python', 70)])

if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)