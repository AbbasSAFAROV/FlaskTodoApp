from flask import Flask , render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Abbas SAFAROV/Desktop/Home/Flask Mini/todo_app/todo.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos = todo.query.all()
    return render_template("index.html",todos =todos)

@app.route("/detail/<string:id>")
def detailTodo(id):
    todo1 = todo.query.filter_by(id=id).first()

    return render_template("detail.html",todo1 = todo1)

@app.route("/complete/<string:id>")
def completeTodo(id):
    todo1 = todo.query.filter_by(id=id).first()
    if(todo1.complete == False):
        todo1.complete = True
    else:
        todo1.complete = False
    
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/delete/<string:id>")
def deleteTodo(id):
    tododetele = todo.query.filter_by(id=id).first()
    db.session.delete(tododetele)
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/add", methods = ["POST"])
def addTodo():
    title = request.form.get("title")
    content = request.form.get("content")
    newTodo = todo(title = title , content = content , complete = False)

    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))

class todo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
    app.run(debug=True)