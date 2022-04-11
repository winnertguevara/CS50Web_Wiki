from django.shortcuts import render
from . import util
from django.http import HttpResponseRedirect,HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import new_page
from django.contrib import messages
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page_title(request,title):
    if util.get_entry(title)==None:
        search = list()
        entries = util.list_entries()
        for entry in entries:
            if title.lower() in entry.lower():
                search.append(entry)

        return render(request, "encyclopedia/list_search.html", {
            "list": search,
            "title": title,
            "empty": len(search),
        })
    else:
        return render(request, "encyclopedia/entry_page.html", {
            "entry": util.get_entry(title),
            "title": title.capitalize(),
        })

def search(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect(request.POST['q'])

def new(request):
    if request.method == "POST":
        entries = util.list_entries()
        for entry in entries:
            if (request.POST['title']).lower() == entry.lower():
                messages.error(request, 'This title already exist')
                return HttpResponseRedirect('/create_page')

        util.save_entry(request.POST['title'], request.POST['content'])
        return HttpResponseRedirect('/wiki/'+request.POST['title'])
    else:
        form = new_page()

    return render(request, "encyclopedia/new_page.html", {'form': form})

def edit(request, title):
    if request.method == "GET":
        form = new_page({'title': title, 'content': util.get_entry(title)})
        return render(request, "encyclopedia/edit_page.html", {'form': form,
                                                               'title': title})
    else:
        util.save_entry(title, request.POST['content'])
        return HttpResponseRedirect('/wiki/' + title)

def random_page(request):
    entries = util.list_entries()
    title = random.choice(entries)
    return render(request, "encyclopedia/entry_page.html", {'title': title,
                                                            'entry': util.get_entry(title),
                                                           })