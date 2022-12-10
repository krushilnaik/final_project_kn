"""
Ascii Djenerator views
"""

import sqlite3

from django.shortcuts import render


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

        with sqlite3.connect('../alphabet.db') as conn:
            for letter in query:
                cur = conn.cursor()
                cur.execute('SELECT * FROM letter WHERE letter = ?', (letter,))

                row = cur.fetchone()

                print(row)

        # art = [request.POST['text'], 'art']

        return render(request, 'generator.html', {'art': art})

    return render(request, 'generator.html')
