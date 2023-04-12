from django.shortcuts import render, redirect
from .models import Pessoa
def minha_view(request):
    print(request.POST)

def home (request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas}) 

def salvar(request):
    op = request.POST.get("op")
    article = request.POST.get("article")
    data = request.POST.get("data")
    nf_fornecida = request.POST.get("nf_fornecida")
    nf_ret = request.POST.get("nf_ret")
    nf_ind = request.POST.get("nf_ind")
    total_received = request.POST.get("total_received")
    first_quality = request.POST.get("first_quality")
    second_quality = request.POST.get("second_quality")
    third_quality = request.POST.get("third_quality")
    timemoney = request.POST.get("timemoney")
    value_pieces = request.POST.get("value_pieces")
    total_value = request.POST.get("total_value")
    payment_status = request.POST.get("payment_status")
    date_shipment = request.POST.get("date_shipment")
    approval_date = request.POST.get("approval_date")
    preview_payment = request.POST.get("preview_payment")
    date_payment = request.POST.get("date_payment")
    
    Pessoa.objects.create(
        op=op, 
        article=article, 
        data=data,
        nf_fornecida=nf_fornecida,
        nf_ret=nf_ret,
        nf_ind=nf_ind,
        total_received=total_received,
        first_quality=first_quality,
        second_quality=second_quality,
        third_quality=third_quality,
        timemoney=timemoney,
        value_pieces=value_pieces,
        total_value=total_value,
        payment_status=payment_status,
        date_shipment=date_shipment,
        approval_date=approval_date,
        preview_payment=preview_payment,
        date_payment=date_payment
    )
    
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'update.html', {"pessoa": pessoa})

def update(request, id):
    op = request.POST.get("op")
    article = request.POST.get("article")
    data = request.POST.get("data")
    nf_fornecida = request.POST.get("nf_fornecida")
    nf_ret = request.POST.get("nf_ret")
    nf_ind = request.POST.get("nf_ind")
    total_received = request.POST.get("total_received")
    first_quality = request.POST.get("first_quality")
    second_quality = request.POST.get("second_quality")
    third_quality = request.POST.get("third_quality")
    timemoney = request.POST.get("timemoney")
    value_pieces = request.POST.get("value_pieces")
    total_value = request.POST.get("total_value")
    payment_status = request.POST.get("payment_status")
    date_shipment = request.POST.get("date_shipment")
    approval_date = request.POST.get("approval_date")
    preview_payment = request.POST.get("preview_payment")
    date_payment = request.POST.get("date_payment")

    pessoa = Pessoa.objects.get(id=id)
    pessoa.op = op
    pessoa.article = article
    pessoa.data = data
    pessoa.nf_fornecida = nf_fornecida
    pessoa.nf_ret = nf_ret
    pessoa.nf_ind = nf_ind
    pessoa.total_received = total_received
    pessoa.first_quality = first_quality
    pessoa.second_quality = second_quality
    pessoa.third_quality = third_quality
    pessoa.timemoney  = timemoney
    pessoa.value_pieces = value_pieces
    pessoa.total_value = total_value
    pessoa.payment_status = payment_status
    pessoa.date_shipment = date_shipment
    pessoa.approval_date = approval_date
    pessoa.preview_payment = preview_payment
    pessoa.date_payment = date_payment
    pessoa.save()

    return redirect('home')

def delete (request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)

def create(request):
    return render(request, 'create.html')