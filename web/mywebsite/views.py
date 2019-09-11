from django.shortcuts import render


def index(request):
    context = {
        'title': 'Savana',
        'heading': 'Selamat Datang',
        'subheading': 'di Savana'
    }
    return render(request, 'index.html', context)
