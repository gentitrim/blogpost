from django.db import models
from django.db.models import CharField,DateTimeField,TextField,ForeignKey,CASCADE,DO_NOTHING

# Create your models here.

class Post(models.Model):
    title = CharField(max_length=100)
    content = TextField(max_length=2000)
    post_time = DateTimeField(auto_now_add=True)
    post_update_time = DateTimeField(auto_now=True)
    author = ForeignKey("Author",on_delete=CASCADE)

    def __str__(self):
        return self.title
    

class Author(models.Model):
    name = CharField(max_length=30)
    lastname  = CharField(max_length=30)
    username = CharField(max_length=30)

    def __str__(self):
        return f"{self.username}"

class Coment(models.Model):
    content = TextField(max_length=2000)
    post_time = DateTimeField(auto_now_add=True)
    post_update_time = DateTimeField(auto_now=True)
    author = ForeignKey("Author",on_delete=DO_NOTHING)
    post = ForeignKey("Post",on_delete=CASCADE)