"""
Cosmetic Insights — companion site
Simple Flask app that serves the static HTML pages and assets
for the Cosmetic Insights Tableau project.

Run locally:
    pip install flask
    python app.py
Then open http://127.0.0.1:5000
"""

from flask import Flask, render_template_string, send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder="assets", static_url_path="/assets")

PAGES = {
    "/": "index.html",
    "/index.html": "index.html",
    "/about.html": "about.html",
    "/dashboard.html": "dashboard.html",
    "/dataset.html": "dataset.html",
    "/story.html": "story.html",
}


def _read_page(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _register_routes():
    for route, filename in PAGES.items():
        def make_view(fname):
            def view():
                return render_template_string(_read_page(fname))
            return view

        endpoint = "page_" + route.replace("/", "_root_") if route == "/" else "page_" + route
        app.add_url_rule(
            route,
            endpoint=endpoint,
            view_func=make_view(filename),
        )


_register_routes()


@app.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory(os.path.join(BASE_DIR, "assets"), filename)


if __name__ == "__main__":
    app.run(debug=True)
