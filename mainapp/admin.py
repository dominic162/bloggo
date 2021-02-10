from django.contrib import admin
from mainapp import models

# Register your models here.
admin.site.register([
    models.blog,
    models.writer,
    models.contact
    ])