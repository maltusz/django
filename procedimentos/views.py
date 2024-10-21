import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Procedimento, Dentista
from django.contrib.auth.decorators import login_required 

@login_required
def index(req):
    return render(req, "procedimentos/index.html")

@login_required
def listar(req):
    proc = Procedimento.objects.all()
    return render(req, "procedimentos/listar.html", {"procedimentos": proc})

@login_required
def adicionar(req):
    if req.method == "POST":
        try:
            data = json.loads(req.body)
            id_dentista = data.get('dentista')

            dentista_instance = Dentista.objects.get(id=id_dentista)

            proc = Procedimento(
                nome_paciente=data.get('name'),
                procedimento=data.get('procedimento'),
                data_procedimento=data.get('date'),
                valor_procedimento=data.get('valor'),
                dentista=dentista_instance
            )

            try:
                proc.save()
                return JsonResponse({'message': 'Procedimento adicionado com sucesso!', 'status': True})
            except Exception as e:
                return JsonResponse({'error': str(e), 'status': False}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido', 'status': False}, status=400)
    
    d = Dentista.objects.all()
    return render(req, "procedimentos/adicionar.html", {"dentistas": d})

@login_required
def editar(req, id):
    if req.method == "GET":
        d = Dentista.objects.all()
        procedimento = Procedimento.objects.get(id=id)
        procedimento.valor_procedimento = str(procedimento.valor_procedimento).replace(',', '.')
        return render(req, "procedimentos/editar.html", {"p": procedimento, "dentistas": d})
    
    elif req.method == "POST":
        p = Procedimento.objects.get(id=id)
        data = json.loads(req.body)
        print(data)
        id_dentista = data.get('dentista')

        dentista_instance = Dentista.objects.get(id=id_dentista)

        p.nome_paciente=data.get('name')
        p.procedimento=data.get('procedimento')
        p.data_procedimento=data.get('date')
        p.valor_procedimento=data.get('valor')
        p.dentista=dentista_instance

        try:
            p.save()
            return JsonResponse({'message': 'Procedimento alterado com sucesso!', 'status': True})
        except Exception as e:
            return JsonResponse({'error': str(e), 'status': False}, status=400)