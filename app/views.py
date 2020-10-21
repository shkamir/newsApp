from django.shortcuts import render, get_object_or_404
from .models import News, Blog, NazarSanji
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request, 'base.html')

def more_news(request, id=None, title=None):
    """ gets id from get absolute url in News model """
    news = get_object_or_404(News, id=id, title=title)
    context = {
        "title": news.title,
        "news": news
    }
    return render(request, 'news_detail.html',context=context)

def news(request):
    """ Handles News Model """

    # old = News.objects.filter(id=3).update(title="this title has changed because id was 3 :)")
    news = News.objects.all().order_by('-publish')
    context = {
        "title": "news page",
        "news": news
    }
    return render(request, 'news.html', context=context)


def more_blogs(request,id=None, name=None):
    blog = get_object_or_404(Blog, id=id, name=name)
    context = {
        "title": blog.name,
        "blog": blog
    }
    return render(request, 'blogs_detail.html', context)

def blog(request):

    """ Handles Blog Model """
    blog = Blog.objects.all().order_by('-id')
    context = {
        "title": "blog page",
        "blog": blog
    }
    return render(request, 'blog.html', context)


def comment(request):
    """ handels comments """
    if request.method == "POST":
        # print (request.POST)
        this_comment = request.POST.get("cm")
        # print (comment)
        myCm = NazarSanji(comment=this_comment)
        myCm.save()
    
    messages.success(request, "SENT")
    return render(request, "nazarha.html")