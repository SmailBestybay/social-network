from flask import Flask, redirect, render_template, request, session
from helper import search_unogs
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    
    title = request.form.get("search")
    result = search_unogs(title)

    # if no results
    if "results" not in result:
        return render_template("no_results.html")

    result_only = result["results"]
    
    # concatenate clist with {} then use json.loads() to convert it to dict
    
    for i in range(len(result_only)):    
        result_only[i]["clist"] = "{" + result_only[i]["clist"] + "}"
        result_only[i]["clist"] = json.loads(result_only[i]["clist"])

        # for key and value in clist, lower and replace whitespace with dash
        for key, value in result_only[i]["clist"].items():
            result_only[i]["clist"][key] = value.replace(" ", "-")

    return render_template("results.html", result_only=result_only)