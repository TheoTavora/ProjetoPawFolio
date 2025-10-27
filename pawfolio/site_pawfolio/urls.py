from django.urls import path
from . import views
from .views import login_view, logout_view, cadastro_view, pet_novo_view, responder

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", cadastro_view, name="cadastro"),
    path("logout/", logout_view, name="logout"),
    path("login/", login_view, name="login"),
    path("agendamentos/", views.agendamentos_view, name="agendamentos_view"),
    path("cadastropet/", pet_novo_view, name="cadastropet_view"),
    path("petshops/", views.petshop_list, name="petshop_list"),
    path("petshops/novo/", views.petshop_create, name="petshop_create"),
    path("chatbot/", views.chatbot_view, name="chatbot_view"),
    path("responder/", responder, name="responder"),
    path("clientes/", views.cliente_list, name="cliente_list"),
    # ex: páginas públicas
]
