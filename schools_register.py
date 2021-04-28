from flask import Flask, render_template, redirect, request
import psycopg2
import os

app = Flask(__name__)
schools_register = []
DB_USERNAME = os.environ["SCHOOLS_REGISTER_DB_USERNAME"]
DB_PASSWORD = os.environ["SCHOOLS_REGISTER_DB_PASSWORD"]
DB_HOSTNAME = os.environ["SCHOOLS_REGISTER_DB_HOSTNAME"]
DB_PORT = os.environ["SCHOOLS_REGISTER_DB_PORT"]
DB_NAME = os.environ["SCHOOLS_REGISTER_DB_NAME"]
POSTGRESQL_URI = "postgres://{}:{}@{}:{}/{}".format(
    DB_USERNAME,
    DB_PASSWORD,
    DB_HOSTNAME,
    DB_PORT,
    DB_NAME
)

connection = psycopg2.connect(POSTGRESQL_URI)

@app.route("/test")
def test():
    return render_template("table.j2")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO schools (school_name, principal_name, school_address, students) VALUES (%s, %s, %s, %s);",
                    (
                        request.form.get("school_name"),
                        request.form.get("principal_name"),
                        request.form.get("school_address"),
                        request.form.get("students")
                    )
                )
        return redirect("/results")
    return render_template("form.j2")

@app.route("/results")
def results():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM schools;")
            data = cursor.fetchall()
    return render_template("table.j2", data=data)

@app.route("/add")
def add():
    return render_template("add.j2")

@app.route("/edit/<id>", methods=["GET"])
def edit(id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM schools WHERE school_id = {};".format(id))
            data = cursor.fetchall()
    return render_template("edit.j2", data=data[0])

@app.route("/edit/<id>", methods=["POST"])
def update(id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE schools SET school_name = %s, principal_name = %s, school_address = %s, students = %s WHERE school_id = %s;",
            (
                request.form.get("school_name"),
                request.form.get("principal_name"),
                request.form.get("school_address"),
                request.form.get("students"),
                id
            ))
    return redirect("/results")

@app.route("/delete/<id>")
def delete(id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM schools WHERE school_id = {};".format(id))
    return redirect("/results")

@app.route("/search")
def search():
    print(type(request.args.get("school_search")))
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM schools WHERE school_name ILIKE '%{}%';".format(request.args.get("school_search")))
            data = cursor.fetchall()
    return render_template("table.j2", data=data)