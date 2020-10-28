from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Blog, NazarSanji, Contact
from django.contrib import messages
from django.db.models import Q
from .forms import ContactForm, RegisterForm

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


def search(request):
    query = request.GET.get("q")
    button = request.GET.get("submitbutton")
    category = request.GET.get("category")
    # TODO: make the choice to the client to search in blogs or news
    if query is not None:
        if category == "news":
            lookup = Q(title__icontains=query)
            result = News.objects.filter(lookup)
            context = {
                "result": result,
                "button": button,
            }
            return render(request,"seach.html", context)
        elif category == "blog":
            lookup = Q(name__icontains=query)
            result = Blog.objects.filter(lookup)
            context = {
                "result": result,
                "button": button,
            }
            return render(request,"seach.html", context)            

    return render(request,"seach.html")


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES or None) 
        form.save()    
        name=form.cleaned_data.get("name")
       	messages.success(request,"successfilly sent")
        client = Contact.objects.filter(name=name)
        form = ContactForm()
        redirect("app1:contact")
        return render(request, "contact.html", {"form": form, "client":client})
    else:
    	return render(request, "contact.html", {"form": form})

def register(request):
    """ handles register """
    form = RegisterForm()
    
    if request.method == "POST":
        # code
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, " Successfull.")
            return redirect('app1:home')
        else:
            messages.error(request, " Failed.")
            redirect('app1:register', messages)

        print ("this is %s" % request.method)

        context = {
            "form": form   
        }
        return render(request, 'register.html', context)


    context = {
        "form": form   
    }
    return render(request, 'register.html', context)