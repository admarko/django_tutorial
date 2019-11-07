To see DB:
`sqlite3 db.sqlite3`
> `.schema`

use python3 for everything


the three-step guide to making model changes:
- Change your models (in models.py).
- Run `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate` to apply those changes to the database.

To get into the shell, run:
- `python manage.py shell`



### TODO:

- add mypy
- add isort
- deal with pycache stuff in in .gitignore
- move sKey from settings -> .env
