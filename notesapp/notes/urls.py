from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    # example: /
    path("", views.index, name="index"),
    # example: /5/
    path("<int:note_id>/", views.detail, name="detail"),
    # example: /login/
    path("login/", LoginView.as_view(template_name="notes/login.html"), name="login"),
    # example: @login_required
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    # example: /delete/5/
    path("delete/<int:note_id>/", views.delete, name="delete")
]
