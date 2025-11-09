# Customer Reviews (Django + DRF)

Simple, free, local project to manage customer reviews.  
Stack: Django, Django REST Framework, SQLite.

## Quickstart
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install django djangorestframework
django-admin startproject config .
python manage.py startapp reviews
# (Models, views, URLs and templates are already included in this repo)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Endpoints

HTML list: GET /reviews/

API list/create: GET, POST /api/reviews/

API detail: GET /api/reviews/<id>/

Admin: GET /admin/

Example (curl)
curl -X POST http://127.0.0.1:8000/api/reviews/ \
  -H "Content-Type: application/json" \
  -d '{"author_name":"Alice","rating":5,"comment":"Great!"}'

curl http://127.0.0.1:8000/api/reviews/

Tests
python manage.py test

Project structure (key parts)
config/                 # Django project
reviews/                # App
  models.py             # Review model
  views.py              # HTML list view
  api.py                # API views (List/Create, Detail)
  serializers.py        # DRF serializer
  templates/reviews/    # list.html

Notes

100% local and free (no paid services).

SQLite by default. Suitable for portfolio demos.