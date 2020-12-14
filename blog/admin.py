from django.contrib import admin

from .models import Author, Tag, News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published', 'author')
    search_fields = ('title', 'author')


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(News, NewsAdmin)
