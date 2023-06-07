from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import AddForm

def minha_view(request):
    print(request.POST)

def home (request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas}) 

def create(request):
    if request.method == 'POST': 
        form=AddForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('home')
    else:
        
        form=AddForm()
        return render(request, 'create.html', {"form": form})

def update(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST': 
        form=AddForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()

        return redirect('home')
    else:
        
        form=AddForm(instance=pessoa)
        return render(request, 'update.html', {"form": form, "pessoa": pessoa})
        
    

def delete (request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)


def exibir_pagina(request):
    return render(request, 'order-of-production/real_time_production.html')
