from flask import Flask, render_template, jsonify
from pages import PAGES

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", pages=PAGES, total=len(PAGES))


@app.route("/api/pages")
def api_pages():
    return jsonify(PAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
