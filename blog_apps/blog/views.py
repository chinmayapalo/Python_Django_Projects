from django.shortcuts import render
from django.views.generic import  ListView,DetailView
from .models import post

# Create your views here.

class BlogPageView(ListView):
    model = post
    template_name = 'blog.html'
    context_object_name = 'all_blog_list'
    queryset = post.objects.all().order_by("-date")[:25]


#
# class BlogDescView(DetailView):
#     model = post
#     template_name = 'post.html'



def BlogDescView(request,id):
    posts = post.objects.get(id=id)
    context = {
        'post': posts
    }
    return render(request, 'post.html', context)
