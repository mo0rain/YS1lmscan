from flask import Flask,render_template,request,jsonify
from markupsafe import escape

app = Flask(__name__,instance_relative_config=True , template_folder="templates")
app.debug = True

@app.route("/")
def index():
    return "hello world"





@app.route('/test/<name>',methods=['GET', 'POST'])
def test(name):
    if request.method == 'POST':
        return "this is post" + name
    else:
        return "this is get,{}".format(name)


@app.route("/login",methods=['GET', 'POST'])
def login():
    data = request.args
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

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5656)
