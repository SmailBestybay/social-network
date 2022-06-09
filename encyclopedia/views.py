from random import random
from turtle import end_fill, title
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms

from markdown2 import Markdown

from . import util
# import encyclopedia
import random

class NewPageForm(forms.Form):
    newtitle = forms.CharField(label="Title", max_length=30)
    newentry = forms.CharField(label="Markdown Content", widget=forms.Textarea)

class EditPageFrom(forms.Form):
    editarea = forms.CharField(label="Markdown Content", widget=forms.Textarea, initial="entry's markdown text")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, TITLE):
    if util.get_entry(TITLE) is None:
        return render(request, "encyclopedia/error.html", {
            "errormessage": "Error 404: Entry not found"
        })

    # need to use safe filter to escape string quotes in the template
    return render(request, "encyclopedia/entry.html", {
        "entry": Markdown().convert(util.get_entry(TITLE)),
        "title": TITLE
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

def randompage(request):
    random_int = random.randint(0, len(util.list_entries())-1)
    return redirect("entry", util.list_entries()[random_int])

def newpage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            newtitle = form.cleaned_data["newtitle"]
            newentry = form.cleaned_data["newentry"] 
            # check if entry exists
            for entry in util.list_entries():
                if newtitle.lower() == entry.lower():
                    return render(request, "encyclopedia/error.html", {
                        "errormessage": "Entry already exists"
                    })
            # careful, save entry might overwrite old entry without previous checks
            util.save_entry(newtitle, newentry)
            return redirect("entry", newtitle)

    else:
        form = NewPageForm()

    return render(request, "encyclopedia/newpage.html", {
        "form" : form
    })

def editpage(request, TITLE):
    if request.method == "POST":
            form = EditPageFrom(request.POST)
            if form.is_valid():
                editedentry = form.cleaned_data["editarea"]
                util.save_entry(TITLE, editedentry)
                return redirect("entry", TITLE)

    else:
        form = EditPageFrom()
        # prepopulate text area with initial data
        form.fields["editarea"].initial = util.get_entry(TITLE)
    return render(request, "encyclopedia/editpage.html", {
        "form": form,
        "title": TITLE
    })

