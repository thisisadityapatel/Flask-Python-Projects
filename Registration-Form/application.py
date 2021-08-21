from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

# storing all the sports into a list in python
SPORTS=[
    "Cricket",
    "Football",
    "Soccer",
    "Rugby",
    "Hockey",
    "Badminton",
    "Tennis",
    "Basketball"
]

open("froshim1.db", "w").close()
db=SQL("sqlite:///froshim1.db")

db.execute("CREATE TABLE students( name TEXT NOT NULL, sport TEXT NOT NULL);")

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name")
    sport = request.form.get("sport")

    if not name:
        return render_template("error.html", message="No Name Entered")
    if not sport:
        return render_template("error.html", message="No Sport Entered")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid Sport Entered")

    db.execute("INSERT INTO students (name, sport) VALUES(?, ?);", name, sport)

    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    temp = db.execute("SELECT * FROM students")
    return render_template("registrants.html", students=temp)

