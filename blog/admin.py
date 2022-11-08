from django.contrib import admin

# Import Models
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.

# Register your entity here
admin.site.register(Category)
admin.site.register(Article)
