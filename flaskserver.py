from flask import Flask, render_template, redirect, url_for, request, session, make_response
from modules import dbModule

app = Flask(__name__)

app.secret_key = "software_engineering"
lst = []
dict = {}
user = {}

db_class= dbModule.Database()

@app.route("/user")
def userindex():
    sql = "SELECT ID, pwd FROM user"
    db_class.execute(sql)
    results = db_class.cursor.fetchall()
    #db_class.commit()
    for i in results:
        user[i['ID']] = i['pwd']
    if 'username' in session:
        return redirect(url_for("homepage"))
    return render_template("welcome.html")

@app.route("/user/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        if (request.form['username'] in user.keys() and request.form['password'] == user[request.form['username']]):
            session['username'] = request.form['username']
            return redirect(url_for("userindex"))
        else:
            return render_template("index.html")
    return render_template("login.html")

@app.route("/user/register", methods = ["POST","GET"])
def register():
    if request.method == "POST":
        try:
            sql = "INSERT INTO user (ID, pwd) \
                        VALUES (%s, %s)"
            val = (request.form["ID"],request.form['pwd'])
            db_class.execute(sql, val)
            db_class.commit()
    
            user[request.form["ID"]] = request.form['pwd']
            return '''<a href="{{url_for("login")}}"> <script type="text/javascript">alert("Registration completed successfully!");window.location.href = "http://127.0.0.1:5000/user/login";</script>'''
        except:
            return '''<a href="{{url_for("register")}}"> <script type="text/javascript">alert("ID already exists!");window.location.href = "http://127.0.0.1:5000/user/register";</script>'''
    return render_template("register.html")



@app.route("/user/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for("userindex"))

@app.route("/user/homepage", methods = ["POST", "GET"])
def homepage():
    if request.method == "POST":
        if (request.form.getlist("chk") != []):
            sql = "DELETE FROM diary \
                    WHERE title = %s AND ID = %s"
            lst = request.form.getlist("chk")
            print(dict)
            print(lst)
            for i in lst:
                val = (i, session['username'])
                del(dict[i])
                db_class.execute(sql, val)
                db_class.commit()

    sql = "SELECT title, content, filepath FROM diary WHERE ID = %s"
    db_class.execute(sql, session['username'])
    results = db_class.cursor.fetchall()
    #db_class.commit()
    for i in results:
        dict[i['title']] = [i['content'], i['filepath']]
    return render_template("homepage.html", result = dict)

@app.route("/user/addpost")
def addpost():
    return render_template("addpost.html")

@app.route("/user/deletepost", methods = ["POST", "GET"])
def deletepost():
    if request.method == "POST":
        session["chk"] = request.form["chk"]
    return render_template("homepage.html", result = dict)

@app.route("/user/choosedelete")
def choosedelete():
    return render_template("deletepost.html", result = dict)

@app.route("/user/editpost/<titlename>")
def editpost(titlename):
    return render_template("editpost.html", name = titlename, value = dict[titlename])

@app.route("/user/showpost/<titlename>")
def showpost(titlename):
    return render_template("showpost.html", name = titlename, value = dict[titlename])


@app.route("/user/savepost", methods = ["POST", "GET"])
def savepost():
    if request.method == "POST":
        session["title"] = request.form['title']
        session['content'] = request.form['content']
        session['filename'] = request.form['filename']

        if(session["title"] in dict.keys()):
            sql = "UPDATE diary SET title = %s, content = %s, filepath = %s \
                WHERE title = %s"
            val = (session["title"],session['content'],session['filename'], session["title"])

        else:
            sql = "INSERT INTO diary (ID, title, content, filepath) \
                    VALUES (%s, %s, %s, %s)"
            val = (session['username'], session["title"],session['content'],session['filename'])
        db_class.execute(sql, val)
        db_class.commit()


        dict[session["title"]] = [session['content'], session['filename']]

    return redirect(url_for("homepage"))

if __name__ == '__main__':
    app.run(debug=True)