"""
Ascii Djenerator views
"""

from django.shortcuts import render


# Create your views here.
def index(request):
    """
    Home page: GET /
    """

    return render(request, 'index.html')
