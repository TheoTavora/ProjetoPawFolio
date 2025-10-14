from django.urls import path
from . import views
from .views import login_view, logout_view, cadastro_view, pet_novo_view

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", cadastro_view, name="cadastro"),
    path("logout/", logout_view, name="logout"),
    path("login/", login_view, name="login"),
    path("agendamentos/", views.agendamentos_view, name="agendamentos_view"),
    path("cadastropet/", pet_novo_view, name="cadastropet_view"),
    # ex: páginas públicas
]
