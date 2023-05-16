from django.shortcuts import render

def homepage(request):
    return render(request, 'common/homepage.html', {
        'title': "Shield Homepage",
        })
