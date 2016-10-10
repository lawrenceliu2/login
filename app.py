import util.login

from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

app.secret_key="asdfghjkl"

@app.route("/")
def welcome():
    return render_template("home.html", message="", logged=False)


@app.route("/auth", methods=["POST"])
def authenticate():
    if util.login.verifyUser(request.form["username"]) and util.login.verifyPass(request.form["username"], request.form["password"]):
        session["username"] = request.form["username"]
        return render_template("home.html", logged=True)
    else:
        if util.login.verifyUser(request.form["username"]):
            return render_template("results.html", authed=False, why="Password incorrect!")
        else:
            return render_template("results.html", authed=False, why="Account not found! Please register!")
        

@app.route("/register", methods=["POST"])
def register():
    if "username" in request.form.keys():
        if util.login.registered(request.form["username"], request.form["password"]):
            print "Register complete"
            return render_template("home.html", message="Account registered. Please log in.", logged=False)
        else:
            print "register failed"
            return render_template("home.html", message="Sorry, that username is taken already.", logged=False)
    else:
        print request.form
        return redirect(url_for("welcome"))
        #return render_template("home.html", message="", logged=False)

@app.route("/jacobo")
def js():
    print url_for("js")
    return redirect(url_for(""))


@app.route("/logout", methods=["POST"])
def done():
    session.pop("username")
    return redirect(url_for("welcome"))
    #return render_template("home.html", logged=False, message="Logged out successfully.")


if __name__=="__main__":
    app.debug = True
    app.run()
