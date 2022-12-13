"""
Initial database seeder
"""

from pathlib import Path

from django.core.management.base import BaseCommand

from ascii_djenerator.models import Letter


class Command(BaseCommand):
    """
    Define file as management command
    """

    def handle(self, *args, **options):
        run_seed()


def clear_data():
    """
    Deletes all the table data
    """

    print("Clearing letter table...")

    Letter.objects.all().delete()

    print("Letter table cleared")


def run_seed():
    """
    Seed the database
    """

    clear_data()

    alphabet_file = Path(__file__).parent / "alphabet.txt"

    try:
        print("Trying to seed database...")

        with open(alphabet_file, encoding="utf-8") as alphabet:
            letter = ""
            representation = ""

            for line in alphabet:
                if line[0].isdigit():
                    if letter != "":
                        # add the freshly-built letter to the database
                        temp = Letter(
                            letter=letter,

                            # [:-1] gets rid of the trailing "|"
                            representation=representation[:-1]
                        )

                        temp.save()

                    # gets the second half of the line, without the quotes
                    # e.g. 33 '!' -> !
                    letter = line.split(" ", 1)[-1].strip()[1:-1]

                    # reset the representation string
                    representation = ""
                    continue

                representation += f"{line.strip()}|"

            print("Successfully seeded database")
    except FileNotFoundError:
        print("'alphabet.txt' not found")
