"""
Ascii Djenerator views
"""

# import sqlite3

from django.shortcuts import render

from .models import Letter


# Create your views here.
def index(request):
    """
    Home page: GET /
    """

    return render(request, 'index.html')


def generator(request):
    """
    The generator page
    """

    if request.method == 'POST':
        query = request.POST['text']

        art = []

        for letter in query:
            representation: str = Letter.objects.get(
                letter=letter
            ).representation

            art.append(representation.split('|'))

        art = ["".join(line) for line in zip(*art)]

        return render(request, 'generator.html', {'art': art})

    return render(request, 'generator.html')
