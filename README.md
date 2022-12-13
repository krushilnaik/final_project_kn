# Ascii Djenerator

## Table of Contents
- [Ascii Djenerator](#ascii-djenerator)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)

## Usage

First, make sure you have Python 3.7+ installed

Run `pip install -r requirements.txt` to install all the dependencies

To initialize the database and seed the Letters table:

```
python manage.py makemigrations
python manage.py migrate
python manage.py seed
```

Run the app with `python ./manage.py runserver`
