from .models import Letter


def build_art(word: str):
    art = []

    for letter in word:
        representation: str = Letter.objects.get(
            letter=letter
        ).representation

        art.append(representation.split('|'))

    art = ["".join(line) for line in zip(*art)]

    return art
