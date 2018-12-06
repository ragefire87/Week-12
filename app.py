from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    return render_template("index.html", entries=model.get_entries())

@app.route("/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

@app.route("/admin")
def admin():
    model.init()
    ## add a guestbook entry
    return render_template("admin.html", entries=model.get_entries())

@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    return redirect("/")

@app.route("/delete", methods=["GET","POST"])
def deleteentry():
    if request.method == "POST":
        counter = request.form["id"]
        model.delete_entry(counter)
    else:
        model.get_entries()
    return redirect("/admin")

if __name__=="__main__":
    model.init()
    app.run(debug=True)
