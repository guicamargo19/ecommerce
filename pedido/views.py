from django.http import HttpResponse
# from django.shortcuts import render
from django.views import View


class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')


class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('SalvarPedido')


class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
