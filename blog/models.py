from django.db import models
from tinymce import models as tinymce_models

# Create your models here.

class Category(models.Model):
    name = models.CharField("article category", max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Article(models.Model):
    title = models.CharField(max_length = 255, null = False, blank = False)
    slug = models.SlugField(max_length = 255, null = False, blank = False)
    # TINYMCE Plugin
    description = tinymce_models.HTMLField()
    likes = models.IntegerField(default=0)
    
    # Thumbnail Image
    image = models.ImageField(upload_to="uploads/% Y/% m/% d/")
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = "article categorizations")
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    # Number of likes in a post
    def get_number_of_likes(self):
        return self.likes

class Myself(models.Model):
    name = models.CharField(max_length =75, null=False, blank=False)
    profile_picture = models.ImageField(upload_to="uploads/me/")
    pass
    # Profile picture
    
    def __str__(self):
        return self.name
