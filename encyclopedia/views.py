from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from . import util
import encyclopedia


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, TITLE):
    if util.get_entry(TITLE) is None:
        return render(request, "encyclopedia/error.html")

    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(TITLE)
        })

def search(request):
    if 'q' in request.GET:
        return render(request, "encyclopedia/entry.html", {
            "entry" : util.get_entry(request.GET['q'])
        }) 
    



