# Django tutorial

The tutorial by [Django Girls](https://tutorial.djangogirls.org/en/) looks great, let's follow it.

### Start the project

More info [here](https://tutorial.djangogirls.org/en/django_start_project/)

Move in the project folder and run

```bash
django-admin startproject mysite .
```

Open `mysite/settings.py`:

Add timezone/language info
```python
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-ch'
```

Setup the root for the static files

```python
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
```

Add the hosting site

```python
ALLOWED_HOSTS = ["127.0.0.1", ".pythonanywhere.com", ".netlify.com"]
```

Create the default database
```bash
python manage.py migrate
```

Start the server
```bash
python manage.py runserver
```

And check it out: [127.0.0.1:8000](http://127.0.0.1:8000/)

### Django models

More info [here](https://tutorial.djangogirls.org/en/django_models/)

Create the blog application inside the project, where `blog` is the app name

```bash
python manage.py startapp blog
```

In `mysite/settings.py`, add the app. Note that `BlogConfig` is a method inside `blog/apps.py`.

```python
INSTALLED_APPS = [
    ...
    "blog.apps.BlogConfig",
]
```

In `blog/models.py`, create the model for a blog post, where `Post` is the model name

```python
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

Add the model to the database
```bash
python manage.py makemigrations blog
python manage.py migrate blog
```

### Django admin

More info [here](https://tutorial.djangogirls.org/en/django_admin/)

Register the model on the admin site, in `blog/admin.py`

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Create a superuser
```bash
python manage.py createsuperuser
```

Login in the admin page: (http://127.0.0.1:8000/admin/) and create a few posts.

### Deploy!

More info [here](https://tutorial.djangogirls.org/en/deploy/)
