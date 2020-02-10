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

On [Python Anywhere](https://www.pythonanywhere.com/) there is a magic script

```bash
pip3.6 install --user pythonanywhere
pa_autoconfigure_django.py --python=3.6 https://github.com/<your-github-username>/my-first-blog.git
```

Remember that the database is a different one, so a new superuser has to be created.

### Django urls

More info [here](https://tutorial.djangogirls.org/en/django_urls/)

Urls are set up in `mysite/urls.py`

The admin URL is already setup. For every URL that starts with `admin/`, Django will wind a corresponding view.

```python
path("admin/", admin.site.urls),
```

Link the blog urls to the root of the site, saved in `blog/urls.py`

```python
path("", include("blog.urls")),
```

Import the views from the blog app, and link `view.post_list` to the root URL, with the name `/post_list`

```python
from . import views
path("", views.post_list, name="post_list"),
```

### Django views

More info [here](https://tutorial.djangogirls.org/en/django_views/)

The view holds the logic of the application.
It will request information from the model and pass it to a template.

Inside `blog/views.py` define the `post_list` view defined above to the template in `blog/templates/blog/post_list.py`

```python
def post_list(request):
    return render(request, "blog/post_list.html", {})
```

### Django QuerySets

More info [here](https://tutorial.djangogirls.org/en/django_orm/)

Open the Django interactive console with

```bash
python manage.py shell
```

And use it to inspect the data in your database

```python
# import the models
from blog.models import Post
from django.contrib.auth.models import User

# list all the posts and users
Post.objects.all()
User.objects.all()

# get the user
me = User.objects.get(username="pitrified")
# create a post
Post.objects.create(author=me, title="Sample title", text="Test")

# filter the results
Post.objects.filter(author=me)
# notice __operator syntax
Post.objects.filter(title__contains="title")

# easy timezones
from django.utils import timezone
Post.objects.filter(published_date__lte=timezone.now())

# publish the post to see it if you filter by date
post = Post.objects.get(title="Sample title")
post.publish()

# order the results
Post.objects.order_by("created_date")
Post.objects.order_by("-created_date")

# chain queries
Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
```

### Dynamic data in templates

More info [here](https://tutorial.djangogirls.org/en/dynamic_data_in_templates/)

Inside `blog/views.py` the actual posts have to be extracted and sent to the template.
Notice that `'posts'` is the key of the dict, and will be used in the template.

```python
def post_list(request):
    show_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, "blog/post_list.html", {"posts": show_posts})
```

### Use the data in the template

More info [here](https://tutorial.djangogirls.org/en/django_templates/)

In the template file `blog/templates/blog/post_list.html`

```html
<div>
    <h1><a href="/">Django Girls Blog</a></h1>
</div>

{% for post in posts %}
    <div>
        <p>published: {{ post.published_date }}</p>
        <h2><a href="">{{ post.title }}</a></h2>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
{% endfor %}
```









