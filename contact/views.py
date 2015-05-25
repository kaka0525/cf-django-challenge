from django.shortcuts import render, get_object_or_404
from .models import User
from .forms import UserForm, JoinForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'index.html', {'user_list': User.objects.all()})


def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'detail.html', {'user_list': User.objects.all()})


def create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        print "attempting to create user"
        user, created = User.objects.get_or_create(
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            email=form.cleaned_data["email"],
            content=form.cleaned_data["content"],
            location=form.cleaned_data["location"],
            title=form.cleaned_data["title"])
        user.save()
    return HttpResponseRedirect("/contact/")


def edit(request, user_id):
    return render(
        request, 'edit.html',
        {'user': get_object_or_404(User, pk=user_id)})


def save_edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if 'delete' in request.POST:
        user.delete()
    else:
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        user.content = request.POST["content"]
        user.location = request.POST["location"]
        user.title = request.POST["title"]
        user.save()
    return HttpResponseRedirect("/contact/")
