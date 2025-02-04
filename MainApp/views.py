from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from MainApp.models import Snippet, User
from MainApp.forms import SnippetForm, UserRegistrationForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


@login_required(login_url='main')
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
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user = request.user
                snippet.save()
            return redirect("snippet_list")  # GET snippets/list
        return render(request, 'pages/add_snippet.html', {'form': form})


def snippet_delete(request, item_id):
    item = get_object_or_404(Snippet, id=item_id)
    item.delete()
    return redirect("snippet_list")  # GET snippets/list


def snippet_edit(request, item_id):
    item = get_object_or_404(Snippet, id=item_id)
    # Example 1
    # if request.method == "GET":
    #     context = {
    #         'item': item,
    #         'type': 'edit'
    #     }
    #     return render(request, 'pages/snippet_page.html', context)

    # Example 2
    if request.method == "GET":
        form = SnippetForm(instance=item)
        return render(request, 'pages/add_snippet.html', {'form': form})

    if request.method == "POST":
        form = request.POST
        item.name = form['name']
        item.code = form['code']
        item.public = form.get('public', False)
        item.save()
        return redirect("snippet_list")  # GET snippets/list


def render_snippet_list(request):
    if request.method == 'GET':
        items = Snippet.objects.filter(public=True)
        context = {'items': items}
        return render(request, 'pages/snippet_list.html', context)


def render_snippet_page(request, item_id):
    item = get_object_or_404(Snippet, id=item_id)
    return render(request, 'pages/snippet_page.html', {'item': item})


def render_my_snippets(request, user_id):
    items = Snippet.objects.filter(user_id=user_id)
    context = {
        'pagename': User.objects.get(id=user_id).username,
        'items': items
    }
    return render(request, 'pages/my_snippets.html', context)


def create_user(request):
    if request.method == "GET":
        form = UserRegistrationForm(request.POST)
        return render(request, 'pages/registration.html', {'form': form})

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("main")  # GET snippets/list
        return render(request, 'pages/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            context = {
                'pagename': 'PythonBin',
                'errors': ['Wrong username or password']
            }
            return render(request, 'pages/index.html', context)

    return redirect('main')


def logout(request):
    auth.logout(request)
    return redirect('main')
