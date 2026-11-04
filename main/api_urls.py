from django.urls import path

from main import api_views

app_name = "api"

urlpatterns = [
    path("lakoni/", api_views.lakon_list, name="lakon-list"),
    path("lakoni/<uuid:lakon_id>/", api_views.lakon_detail, name="lakon-detail"),
    path("lakoni/<uuid:lakon_id>/star/", api_views.lakon_star, name="lakon-star"),
]