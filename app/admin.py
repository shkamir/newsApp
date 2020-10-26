from django.contrib import admin

# Register your models here.
from app.models import News, Blog, NazarSanji, Contact


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
class NazarManage(admin.ModelAdmin):
    list_display = ('comment',)
    list_filter = ('now','isRead',)
    search_fields = ('comment',)
    class Meta:
        model = NazarSanji
        
        
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email",)
    list_filter = ("name","email",)
    search_fields = ("name", "message",)
    class Meta:
        model = Contact
        
        
admin.site.register(News, NewsManager)
admin.site.register(Blog, BlogManage)
admin.site.register(NazarSanji, NazarManage)
admin.site.register(Contact, ContactAdmin)

