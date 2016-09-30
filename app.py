from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("login.html")

@app.route("/auth", methods=["POST"])
def authenticate():
    if (request.form["username"]=="harambe" and request.form["password"]=="rip"):
        return render_template("results.html", authed=True)
    else:
        return render_template("results.html", authed=False)


if __name__=="__main__":
    app.debug = True
    app.run()
