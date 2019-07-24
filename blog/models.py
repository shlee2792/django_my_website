from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True)

    slug = models.SlugField(unique=True, allow_unicode=True) #유니코드를 허용한다(한글허용)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/category/{}/'.format(self.slug)

    class Meta:
        verbose_name_plural = 'categories'   ## Categorys -> categories


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/tag/{}/'.format(self.slug)


class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = MarkdownxField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=True)
    head_image = models.ImageField(upload_to='blog/%y/%m/%d/', blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)


    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)


    def get_markdown_content(self):
        return markdown(self.content)

    def get_update_url(self):
         return self.get_absolute_url()+'update/'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
