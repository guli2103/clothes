from django.contrib import admin
from .models import *

@admin.register(Post)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'date', 'use',)

@admin.register(TopPost)
class ArticleTopPost(admin.ModelAdmin):
    list_filter = ('use',) 
    list_display = ('name', 'date', 'use',) 

@admin.register(MainPost)
class ArticleMainPost(admin.ModelAdmin):
    list_filter = ('use',)
    list_display = ('name', 'use', 'date',)      

@admin.register(CatePost)
class ArticleCatePost(admin.ModelAdmin):
    list_filter = ('turi1',)
    list_display = ('turi1', 'soni1',)


@admin.register(LatPost)
class ArticleLatPost(admin.ModelAdmin):
    list_display = ('date',)

