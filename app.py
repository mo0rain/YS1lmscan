from flask import Flask,render_template,request,jsonify,redirect
from markupsafe import escape
import sqlite3


app = Flask(__name__,instance_relative_config=True , template_folder="templates",static_folder="web\static")
app.debug = True

@app.route("/")
def index():
    # return "hello world"
    return redirect("/login")



@app.route('/test/<name>',methods=['GET', 'POST'])
def test(name):
    if request.method == 'POST':
        return "this is post" + name
    else:
        return "this is get,{}".format(name)


@app.route("/login",methods=['GET', 'POST'])
def login():
    # data = request.args
    # print(data.get("name"))
    return render_template("login.html")

@app.route("/admin",methods=['POST'])
def admin():
    data = request.form
    print(data)
    if data['username'] == 'admin' and data['password'] == 'admin':
        return render_template("admin.html")
    else:
        return "FALSE"



# 添加数据
@app.route("/create")
def TestDb():
    return render_template('test/student.html')

# 获取添加的数据,写入的数据库
@app.route('/addstudent',methods = ['POST', 'GET'])
def add_student():
    try:
        nm = request.form['nm']
        addr = request.form['add']
        city = request.form['city']
        pin = request.form['pin']
        with sqlite3.connect("web/static/db/database.db") as con:
           cur = con.cursor()
           cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))
           con.commit()
           msg = "数据添加成功"
    except:
        con.rollback()
        msg = "操作失败"
    finally:
        return render_template("test/result.html",msg = msg)
        con.close()

# 查看数据
@app.route("/show_db")
def ShowDb():
    con = sqlite3.connect("web/static/db/database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    return render_template("test/test1.html",rows = rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5656)
