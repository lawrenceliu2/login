#!/usr/bin/python

import util.login

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("login.html", message="")

@app.route("/auth", methods=["POST"])
def authenticate():
    if util.login.verifyUser(request.form["username"]) and util.login.verifyPass(request.form["username"], request.form["password"]):
        return render_template("results.html", authed=True)
    else:
        if util.login.verifyUser(request.form["username"]):
            return render_template("results.html", authed=False, why="Password incorrect!")
        elif util.login.verifyPass(request.form["username"], request.form["password"]):
            return render_template("results.html", authed=False, why="Username incorrect!")
        else:
            return render_template("results.html", authed=False, why="Account not found! Please register!")

@app.route("/register", methods=["POST"])
def register():
    if "username" in request.form.keys():
        if util.login.registered(request.form["username"], request.form["password"]):
            print "Register complete"
            return render_template("login.html", message="Account registered. Please log in.")
        else:
            print "register failed"
            return render_template("login.html", message="Sorry, that username is taken already.")
    else:
        print request.form
        return render_template("login.html", message="")


if __name__=="__main__":
    app.debug = True
    app.run()
