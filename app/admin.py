from django.contrib import admin

# Register your models here.
from app.models import News, Blog


class NewsManager(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('publish',)
    search_fields = ('title', 'description',)
    class Meta:
        model = News


class BlogManage(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('publish_date',)
    search_fields = ('name', 'content',)
    class Meta:
        model = Blog


admin.site.register(News, NewsManager)
admin.site.register(Blog, BlogManage)
