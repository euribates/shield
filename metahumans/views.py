import csv

from django.shortcuts import render

# Create your views here.


def listado_metahumans(request):
    with open("superheroes.csv", encoding="utf-8") as f:
        r = csv.reader(f, delimiter=";")
        next(r)
        filas = [
            {
                "nombre": tupla[0],
                "nivel": int(tupla[2]),
                "peligroso": int(tupla[2]) >= 50,
            }
            for tupla in r
            ]
        return render(request, 'metahumans/listado.html', {
            "filas": filas
        })
