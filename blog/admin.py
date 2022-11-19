from django.contrib import admin

# Import Models
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your entity here

class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Owner)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)

