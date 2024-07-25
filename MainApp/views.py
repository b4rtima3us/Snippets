from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.core.exceptions import ObjectDoesNotExist


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    # создаем пустую форму при запросе гет
    if request.method == 'GET':
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)

    # получаем данные из формы и создаем новый сниппет в бд
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippet_list")  # GET snippets/list
        return render(request, 'pages/add_snippet.html', {'form': form})


def snippet_delete(request, item_id):
    try:
        item = Snippet.objects.get(id=item_id)
        item.delete()
        return redirect("snippet_list")  # GET snippets/list
    except ObjectDoesNotExist:
        return HttpResponse("Snippet not found")


def render_snippet_list(request):
    if request.method == 'GET':
        items = Snippet.objects.all()
        context = {'items': items}
        return render(request, 'pages/snippet_list.html', context)
    if request.method == 'POST':
        print(request.__dict__)
        return HttpResponse("Snippet not found")

def render_snippet_page(request, item_id):
    try:
        item = Snippet.objects.get(id=item_id)
        return render(request, 'pages/snippet_page.html', {'item': item})
    except ObjectDoesNotExist:
        return HttpResponse("Snippet not found")
