import json

from flask import Flask, render_template, jsonify
from pages import PAGES
from venues import VENUES

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/book")
def book():
    return render_template("book.html", pages=PAGES, total=len(PAGES))


@app.route("/map")
def map_view():
    total_events = sum(len(v["events"]) for v in VENUES)
    return render_template(
        "map.html",
        venues=VENUES,
        venues_json=json.dumps(VENUES),
        total_events=total_events,
    )


@app.route("/api/pages")
def api_pages():
    return jsonify(PAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
