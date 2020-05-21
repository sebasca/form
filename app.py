from flask import Flask
from flask import render_template, request, redirect, url_for
from form import Form
from config import Config
import psycopg2

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    page = request.args.get('page', 1)
    list = request.args.get('list', 20)
    return "Index"
    ...

posts = [1, 2, 3]
@app.route("/posts")
def indexPosts():
    return "{} posts".format(len(posts))

@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        next = request.args.get('next', None)
        save_to_database(name, email, password)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html", form = Form())

def save_to_database(name, email, password):
    connection = psycopg2.connect("host=hagrid.delhelsa.com user=python password=greencore dbname=py02")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE if not exists form (name text, email text, password text)")
    cursor.execute("INSERT INTO form VALUES (%s, %s, %s)",(name, email, password))
    connection.commit()
    cursor.execute("SELECT * FROM form")
    print(cursor.fetchall())
    connection.close()


if __name__ == '__main__':
    app.run()

