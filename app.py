from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
PASSWORD = os.environ.get("PASSWORD", "dev")


class Entry:
    def __init__(self, content, happiness=""):
        self.content = content
        self.happiness = happiness


entries = []


@app.route("/")
def index():
    return render_template("index.html", entries=entries)


@app.route("/add_entry", methods=["POST"])
def add_entry():
    content = request.form.get("content", "").strip()
    happiness = request.form.get("happiness", "").strip()
    if content:
        entries.append(Entry(content, happiness))
    return redirect("/")
