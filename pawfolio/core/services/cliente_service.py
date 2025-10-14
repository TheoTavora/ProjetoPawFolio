# services/cliente_service.py
from core.models import Cliente
from django.db import IntegrityError

def cadastrar_cliente(name, email, senha):
    try:
        return Cliente.objects.create(
            nome=name, email=email, senha=senha
        )
    except IntegrityError:
        return None
