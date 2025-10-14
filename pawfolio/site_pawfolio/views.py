from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from core.services.cliente_service import cadastrar_cliente
from core.models import Cliente, Agendamento, Pet
from datetime import date

def index(request):
    return render(request, "index.html")


def _get_cliente_by_session(request):
    email = request.session.get("user_email")
    if not email:
        return None
    return Cliente.objects.filter(email=email).only("pk","email").first()

def cadastro_view(request):
    if request.method == "POST":
        cliente = cadastrar_cliente(
            request.POST["name"],
            request.POST["email"],
            request.POST["senha"],
        )
        if cliente:
            return redirect("index")  # rota chamada 'login'
        return render(request, "cadastro.html", {"erro": "falha ao cadastrar"})
    return render(request, "cadastro.html")

@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == "POST":
        email = (request.POST.get("email") or "").strip()
        senha = request.POST.get("senha") or ""
        if not email or not senha:
            return render(request, "login.html", {"erro": "preencha e-mail e senha."})

        # valida simples (plaintext)
        cli = Cliente.objects.filter(email=email, senha=senha).only("email","nome").first()
        if cli:
            request.session.cycle_key()
            request.session["user_email"] = cli.email
            request.session["user_nome"]  = cli.nome
            return redirect("index")
        return render(request, "login.html", {"erro": "e-mail ou senha incorretos."})

    return render(request, "login.html")

def logout_view(request):
    for k in ("user_email","user_nome"):
        request.session.pop(k, None)
    request.session.cycle_key()
    return redirect("index")


def agendamentos_view(request):
    if not request.session.get("user_email"):
        # precisa estar logado
        return HttpResponse(
            "<script>alert('Você precisa estar logado para agendar.');"
            "window.location.href='/login/';</script>"
        )

    contexto = {}

    if request.method == "POST":
        pet = request.POST.get("pet") or ""
        petshop = request.POST.get("petshop") or ""
        servico = request.POST.get("servico") or ""
        data = request.POST.get("data") or ""

        if not (pet and petshop and servico and data):
            contexto["erro"] = "Preencha todos os campos."
        else:
            try:
                Agendamento.objects.create(
                    pet=pet,
                    petshop=petshop,
                    servico=servico,
                    data=data,
                    cliente_email=request.session["user_email"]
                )
                contexto["sucesso"] = "Agendamento realizado com sucesso!"
            except Exception as e:
                contexto["erro"] = f"Erro ao salvar: {e}"

    return render(request, "agendamentos.html", contexto)

def pet_novo_view(request):
    # exige login (sessão simples)
    cli = _get_cliente_by_session(request)
    if not cli:
        return HttpResponse(
            "<script>alert('você precisa estar logado para cadastrar um pet.');"
            "window.location.href='/login/';</script>"
        )

    ctx = {"erro":"", "sucesso":""}

    if request.method == "POST":
        nome      = (request.POST.get("nome") or "").strip()
        especie   = (request.POST.get("especie") or "").strip()
        raca      = (request.POST.get("raca") or "").strip()
        sexo      = (request.POST.get("sexo") or "").strip()
        porte     = (request.POST.get("porte") or "").strip()
        nasc_str  = (request.POST.get("nascimento") or "").strip()
        obs       = (request.POST.get("obs") or "").strip()

        if not nome or not especie:
            ctx["erro"] = "preencha pelo menos nome e espécie."
            return render(request, "cadastropet.html", ctx)

        # parse data de nascimento (opcional)
        nasc = None
        if nasc_str:
            try:
                y, m, d = map(int, nasc_str.split("-"))
                nasc = date(y, m, d)
            except Exception:
                ctx["erro"] = "data de nascimento inválida."
                return render(request, "cadastropet.html", ctx)

        try:
            pet = Pet()  # mapeia campos que existirem no seu model
            if hasattr(pet, "nome"):        pet.nome = nome
            if hasattr(pet, "especie"):     pet.especie = especie
            if hasattr(pet, "raca"):        pet.raca = raca
            if hasattr(pet, "sexo"):        pet.sexo = sexo
            if hasattr(pet, "porte"):       pet.porte = porte
            if hasattr(pet, "nascimento"):  pet.nascimento = nasc
            if hasattr(pet, "obs"):         pet.obs = obs

            # vincular ao cliente (tente vários esquemas comuns)
            if hasattr(pet, "cliente"):         pet.cliente = cli
            elif hasattr(pet, "cliente_id"):    pet.cliente_id = cli.pk
            elif hasattr(pet, "cliente_email"): pet.cliente_email = cli.email
            elif hasattr(pet, "owner"):         pet.owner = cli
            elif hasattr(pet, "user"):          pet.user = cli
            elif hasattr(pet, "usuario"):       pet.usuario = cli

            pet.save()
            ctx["sucesso"] = "pet cadastrado com sucesso."
            # opcional: limpar campos do form após sucesso
            return render(request, "cadastropet.html", ctx)
        except Exception as e:
            ctx["erro"] = f"erro ao salvar: {e}"
            return render(request, "cadastropet.html", ctx)

    return render(request, "cadastropet.html", ctx)
