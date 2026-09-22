from django.urls import path
from main.views import (show_main, 
                        show_experience, 
                        show_lakoni, 
                        create_lakon, 
                        update_lakon, 
                        delete_lakon, 
                        get_lakon_json,
                        register,
                        login_user,
                        logout_user)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("lakoni/", show_lakoni, name="show_lakoni"),
    path("lakoni/add/", create_lakon, name="create_lakon"),
    path("lakoni/<uuid:lakon_id>/edit/", update_lakon, name="update_lakon"),
    path("lakoni/<uuid:lakon_id>/delete/", delete_lakon, name="delete_lakon"),
    path("api/lakoni/", get_lakon_json, name="get_lakon_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]