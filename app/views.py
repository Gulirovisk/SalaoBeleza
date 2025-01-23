from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View

class indexView(View):
    def get(self, request):
        profissionais = Profissional.objects.all()
        servicos = Servico.objects.all()
        return render(request, 'index.html' , {'profissionais': profissionais, 'servicos': servicos})