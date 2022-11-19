from django.db import models
from tinymce import models as tinymce_models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField("article category", max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Article(models.Model):
    title = models.CharField(max_length = 255, null = False, blank = False)
    slug = models.SlugField(max_length = 255, null = False, blank = False)
    # TINYMCE Plugin
    description = models.TextField()
    likes = models.IntegerField(default=0)
    
    # Thumbnail Image
    image = models.ImageField(upload_to="uploads/blog-img/", default="uploads/blog-img/404.png", null = True, blank = True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "article_category")
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.title}' 

    class Meta:
        ('-created_at',)

    # Number of likes in a post
    def get_number_of_likes(self):
        return self.likes

    def get_absolute_url(self):
        return reverse("blog:read_article", kwargs={"slug": self.slug})


class Owner(models.Model):
    name = models.CharField(max_length =75, null=False, blank=False)
    profile_picture = models.ImageField(upload_to="uploads/me/", null = True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = "Owner"