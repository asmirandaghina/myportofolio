from django.urls import path
from main.views import show_main, show_experience, show_lakoni

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("lakoni/", show_lakoni, name="show_lakoni"),
]