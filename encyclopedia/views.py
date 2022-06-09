from random import random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from markdown2 import Markdown

from . import util
# import encyclopedia
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, TITLE):
    if util.get_entry(TITLE) is None:
        return render(request, "encyclopedia/error.html")

    # need to use safe filter to escape string quotes in the template
    return render(request, "encyclopedia/entry.html", {
        "entry": Markdown().convert(util.get_entry(TITLE))
        })

def search(request):
    # must have get method stated in html
    # then use request object to gain access to the query
    if 'q' in request.GET:
        if util.get_entry(request.GET['q']) is not None:
            return redirect("entry", request.GET['q']) 
    results = []
    for entry in util.list_entries():
        if request.GET['q'].upper() in entry.upper():
            results.append(entry)
    if len(results) == 0:
        return render(request, "encyclopedia/noresults.html")
    return render(request, "encyclopedia/results.html", {
        "results" : results,
        "q" : request.GET['q']
    })

def randompage(requst):
    random_int = random.randint(0, len(util.list_entries())-1)
    return redirect("entry", util.list_entries()[random_int])

    



