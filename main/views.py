from django.shortcuts import render
from main.models import Experience, Lakon

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

