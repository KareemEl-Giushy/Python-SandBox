# =========================
# -------------
# Config File
# -------------
# =========================
from flask import Flask

skills_app = Flask(__name__)

@skills_app.route("/")
def indexApp():
    return "Hello From Flask Config"

@skills_app.route("/about")
def aboutApp():
    return "Hello From Flask This is About -Eng.Kareem"

if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)