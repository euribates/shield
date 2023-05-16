from django.shortcuts import render

from .models import Metahuman

# Create your views here.

def metahuman_detail(request, pk):
    metahuman = Metahuman.objects.get(id=pk)
    return render(request, 'metahumans/metahuman_detail.html', {
        "metahuman": metahuman, 
    })


def metahumans_list(request):
    metahumans = Metahuman.objects.all()
    return render(request, 'metahumans/metahumans_list.html', {
        "title": "Relación de metahumanos registrados",
        "metahumans": metahumans,
    })
