import json
import os
from functools import wraps

from flask import Flask, render_template, jsonify, session, request, redirect, url_for
from pages import PAGES
from venues import VENUES

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

SITE_PASSWORD = "dg22"


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("authenticated"):
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        if request.form.get("password") == SITE_PASSWORD:
            session["authenticated"] = True
            return redirect(url_for("index"))
        error = "Wrong password, gentleman."

    if session.get("authenticated"):
        return render_template("home.html")
    return render_template("login.html", error=error)


@app.route("/book")
@login_required
def book():
    return render_template("book.html", pages=PAGES, total=len(PAGES))


@app.route("/map")
@login_required
def map_view():
    total_events = sum(len(v["events"]) for v in VENUES)
    return render_template(
        "map.html",
        venues=VENUES,
        venues_json=json.dumps(VENUES),
        total_events=total_events,
    )


@app.route("/api/pages")
@login_required
def api_pages():
    return jsonify(PAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
