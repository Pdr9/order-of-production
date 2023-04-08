from django.shortcuts import render, redirect
from .models import Pessoa

def home (request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas}) 

def salvar(request):
    vnome = request.POST.get("nome")
    vnumero = request.POST.get("numero")
    vdate = request.POST.get("data")
    Pessoa.objects.create(nome=vnome, numero=vnumero, data=vdate)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'update.html', {"pessoa": pessoa})

def update(request, id):
    vnome = request.POST.get("nome")
    vnumero = request.POST.get("numero")
    vdate = request.POST.get("data")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.numero = vnumero
    pessoa.data = vdate
    pessoa.save()
    return redirect(home)

def delete (request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)

def create(request):
    return render(request, 'create.html')