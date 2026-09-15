from django.urls import path
from main.views import show_main, show_experience, show_lakoni, create_lakon

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("lakoni/", show_lakoni, name="show_lakoni"),
    path("lakoni/add/", create_lakon, name="create_lakon"),
]