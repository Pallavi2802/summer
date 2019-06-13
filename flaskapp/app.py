from flask import Flask,render_template
app=Flask(__name__)

#@app.route("/")
#def home():
  #  return "<h1 style='color=red,font-size:50px;'>hello world"

#@app.route("/hello/<user>")
#def hello(user):
 #   return"<h1 style='color:blue'>Hey welcome to my first project {} </h1>".format(user)

#@app.route("/hello/<int:var>")
#def hey(var):
 #   return"<h1 style='color:red'>your marks are:{}</h1>".format(var)

@app.route("/")
def home():
    return render_template("header.html")

@app.route("/<int:var>")
def hey(var):
    return render_template("hello.html",mark=var)



if __name__ == "__main__":
    app.run(host="localhost",port=80,debug=True)