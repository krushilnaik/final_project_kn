"""
Ascii Djenerator views
"""

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .utils import build_art


# Create your views here.
def index(request):
    """
    Home page: GET /
    """

    return render(request, 'index.html')


@login_required(login_url='/auth/login')
def generator(request):
    """
    The generator page
    """

    if request.method == 'POST':
        art = build_art(request.POST['text'])

        return render(request, 'generator.html', {'art': art})

    return render(request, 'generator.html')


@login_required(login_url='/auth/login')
@require_POST
def random(request):
    """
    Generate a random word
    """

    response = requests.get(
        url='https://api.api-ninjas.com/v1/randomword',
        timeout=1000,
        headers={
            'X-Api-Key': 'P6nDiEWzEias+qnnrMReaw==hAaNKc72nVArU8DT'
        },
    )

    data = response.json()

    art = build_art(data['word'])

    return render(request, 'generator.html', {'art': art})
