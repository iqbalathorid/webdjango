from django.shortcuts import render


def index(request):
    context = {
        'title': 'Blog',
        'heading': 'Blog',
        'subheading': 'jurnal Savana',
    }
    return render(request, 'blog/index.html', context)
