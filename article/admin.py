from django.contrib import admin


# Register your models here.
from article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
