from flask import Flask, render_template, request, redirect
from models import db, Task
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@my-db:5432/tasksdb"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# create tables
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        title = request.form["title"]
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()
        return redirect("/")

    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
