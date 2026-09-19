from django.shortcuts import render
from main.models import Experience, Lakon
from django.contrib import messages
from django.shortcuts import redirect
from main.forms import LakonForm
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def show_main(request):
    context = {
        "name": "Asmiranda Ghina",
        "NPM": "2506656482",
        "study_program": "S1 Sistem Informasi",
        "bio": "Ohoi!",
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
    context = {
        "name": "Asmiranda Ghina",
        "lakon_list": Lakon.objects.all(),
    }
    return render(request, "lakoni.html", context)

def create_lakon(request):
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

def update_lakon (request, lakon_id):
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

def delete_lakon(request, lakon_id):
    lakon = get_object_or_404(Lakon, pk=lakon_id)

    if request.method == "POST":
        lakon.delete()
        messages.success(request, "Lakon berhasil dihapus.")
        return redirect("main:show_lakoni")

    return redirect("main:show_lakoni")


