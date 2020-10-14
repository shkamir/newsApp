from django.shortcuts import render, get_object_or_404
from .models import News, Blog


# Create your views here.
def base(request):
    return render(request, 'base.html')

def more_news(request, id=None):
    news = get_object_or_404(News, id=id)
    context = { 
        "news": news
    }
    return render(request, 'news_detail.html',context=context)

def news(request):
    # old = News.objects.filter(id=3).update(title="this title has changed because id was 3 :)")
    news = News.objects.all().order_by('-publish')
    context = {
        "title": "news page",
        "news": news
    }
    return render(request, 'news.html', context=context)


def blog(request):
    old=Blog.objects.filter(name="newwwwww")
    for older in old:

        new=Blog.objects.create(name="new2", content=f"this content created because blog object {older.name} have been deleted")
    old.delete()
    blog = Blog.objects.all().order_by('-id')[:4]
    context = {
        "title": "blog page",
        "blog": blog
    }
    return render(request, 'blog.html', context)
