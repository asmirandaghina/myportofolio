import datetime
from django.shortcuts import render
from main.models import Experience, Lakon
from django.contrib import messages
from django.shortcuts import redirect
from main.forms import LakonForm
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Tak ada sesi masuk atau cookie tak ditemukan')
    context = {
        "name": "Asmiranda Ghina",
        "NPM": "2506656482",
        "study_program": "S1 Sistem Informasi",
        "bio": "Ohoi!",
        "last_login": last_login
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Asmiranda Ghina",
        "education_list": Experience.objects.filter(category="education"),
        "organization_list": Experience.objects.filter(category='organization'),
    }
    return render(request, "experience.html", context)

def show_lakoni(request):
    json_request = get_lakon_json(request)
    lakon_list = serializers.deserialize(
        "json",
        json_request.content.decode("utf-8"),
    )
    lakon_list = [item.object for item in lakon_list]

    context = {
        "name": "Asmiranda Ghina",
        "lakon_list": lakon_list,
        "can_edit": can_edit(request.user),
    }
    return render(request, "lakoni.html", context)

@login_required(login_url="/login/")
def create_lakon(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = LakonForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Hal baru berhasil ditambahkan!")
        return redirect("main:show_lakoni")

    context = {
        "name": "Asmiranda Ghina",
        "form": form,
    }
    return render(request, "lakoni_form.html", context)

@login_required(login_url="/login/")
def update_lakon (request, lakon_id):
    if not can_edit(request.user):
        raise PermissionDenied
    
    lakon = get_object_or_404(Lakon, pk=lakon_id)
    form = LakonForm(request.POST or None, instance=lakon)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Lakon berhasil diperbarui!")
        return redirect("main:show_lakoni")

    context = {
        "name": "Asmiranda Ghina",
        "form": form,
        "is_edit": True,
    }
    return render(request, "lakoni_form.html", context)

@login_required(login_url="/login/")
def delete_lakon(request, lakon_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    lakon = get_object_or_404(Lakon, pk=lakon_id)

    if request.method == "POST":
        lakon.delete()
        messages.success(request, "Lakon berhasil dihapus.")
        return redirect("main:show_lakoni")

    return redirect("main:show_lakoni")

def get_lakon_json(request):
    title_query = request.GET.get("title", "").strip()
    lakon_list = Lakon.objects.all()

    if title_query:
        lakon_list = lakon_list.filter(title__icontains=title_query)

    lakon_json = serializers.serialize("json", lakon_list, use_natural_foreign_keys=True)
    return HttpResponse(lakon_json, content_type="application/json")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan lakukan log masuk.")
        return redirect("main:login")

    context = {
        "name": "Asmiranda Ghina",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, form.get_user())
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Asmiranda Ghina",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, lakon_id):
    lakon = get_object_or_404(Lakon, pk=lakon_id)

    if request.method == "POST":
        if request.user in lakon.starred_by.all():
            lakon.starred_by.remove(request.user)
        else:
            lakon.starred_by.add(request.user)

    return redirect("main:show_lakoni")

def is_editor(user):
    return user.groups.filter(name="Editor").exists()

def can_edit(user):
    return user.is_superuser or is_editor(user)