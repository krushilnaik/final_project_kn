"""
Ascii Djenerator views
"""

# import sqlite3
import os

import requests
from django.shortcuts import redirect, render

from .models import Letter
from .utils import build_art


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
        # query = request.POST['text']

        art = build_art(request.POST['text'])

        # art = []

        # for letter in query:
        #     representation: str = Letter.objects.get(
        #         letter=letter
        #     ).representation

        #     art.append(representation.split('|'))

        # art = ["".join(line) for line in zip(*art)]

        return render(request, 'generator.html', {'art': art})

    return render(request, 'generator.html')


def random(request):
    """
    Generate a random word
    """

    # https://api.api-ninjas.com/v1/randomword

    response = requests.get(
        url='https://api.api-ninjas.com/v1/randomword',
        timeout=1000,
        headers={
            'X-Api-Key': 'P6nDiEWzEias+qnnrMReaw==hAaNKc72nVArU8DT'
            # 'X-Api-Key': os.environ('API_KEY')
        },
    )

    data = response.json()

    art = build_art(data['word'])

    return render(request, 'generator.html', {'art': art})

    # return render(request, 'generator.html', {'art': ['random']})
    # return redirect('generator', {art})
