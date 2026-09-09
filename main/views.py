from django.shortcuts import render
from main.models import Experience

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
        "experience_list": Experience.objects.all(),  
    }
    return render(request, "experience.html", context)


