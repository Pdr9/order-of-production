from django.shortcuts import render

def exibir_pagina(request):
    return render(request, 'real_time_production/real_time_production.html')
