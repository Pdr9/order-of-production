from django.shortcuts import render, redirect
from .models import OrdemdeProducao

def home (request):
    pessoas = OrdemdeProducao.objects.all()
    return render(request, "index.html", {"pessoas": pessoas}) 

def salvar(request):
    vnome = request.POST.get("nome")
    vnumero = request.POST.get("numero")
    OrdemdeProducao.objects.create(nome=vnome, numero=vnumero)
    pessoas = OrdemdeProducao.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = OrdemdeProducao.objects.get(id=id)
    return render(request, 'update.html', {"pessoa": pessoa})

def update(request, id):
    vnome = request.POST.get("nome")
    vnumero = request.POST.get("numero")
    pessoa = OrdemdeProducao.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.numero = vnumero
    pessoa.save()
    return redirect(home)

def delete (request, id):
    pessoa = OrdemdeProducao.objects.get(id=id)
    pessoa.delete()
    return redirect(home)

def create(request):
    return render(request, 'create.html')