from django.shortcuts import render,get_object_or_404
from django.views.generic import (ListView,
                                DetailView,
                                CreateView )
from mainapp import models,forms
from django.http import HttpResponse,HttpResponseRedirect,request
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from math import ceil
from django.template.defaultfilters import slugify


# Create your views here.

def home(request):
    
    obj=models.blog.objects.all().order_by('?')[:10]
    context={
        'objects':obj,
    }
    return render(request,'mainapp/home.html',context)


def blog_view(request,slug):

    objects=get_object_or_404(models.blog,slug=slug)

    context={
        'object':objects,
    }
    return render(request,'mainapp/blogview.html',context)

def writer_view(request,slug):
    
    objects=get_object_or_404(models.writer,slug=slug)

    context={
        'object':objects,
    }    
    return render(request,'mainapp/writer.html',context)
    #except:
    #   return HttpResponseRedirect('/')

def all_blogs(request):
    objects=models.blog.objects.all()
    temp=ceil(len(objects)/8)
    nslides=range(temp)
    context={
        'object':objects,
        'nslides':nslides,
    }
    ex=temp*8-len(objects)
    if(ex!=0):
        extra=models.blog.objects.all()[:ex]
        context['extra']=extra

    return render(request,'mainapp/allblog.html',context)

def about_us(request):
    context={
        'contactform':forms.contact(),
    }
    if(request.method=="POST"):
        contactform=forms.contact(request.POST)
        if(contactform.is_valid()):
            contactform.save()
            return HttpResponseRedirect('/bloggo')
        else:
            context['contactform']=contactform
    return render(request,'mainapp/about.html',context)

def search(request):
    query=request.GET['search_query']
    post1=models.blog.objects.filter(title__icontains=query)
    post2=models.blog.objects.filter(content__icontains=query)
    post3=models.blog.objects.filter(tags__name__icontains=query)
    allpost=post1.union(post2)
    allpost=allpost.union(post3)
    context={
        'allpost':allpost,
        'query':query,
    }
    return render(request,'mainapp/search.html',context)

def tag_search(request,tag_slug):
    allpost=models.blog.objects.filter(tags__slug=tag_slug)
    context={
        'allpost':allpost,
        'tagname':tag_slug,
    }
    return render(request,'mainapp/tagsearch.html',context)

@login_required(login_url='/auth/login')
def create(request):
    context={
            'form':forms.addblog(),
            'contactform':forms.contact(),
            }
    if( request.method=="POST" ):
        request.POST=request.POST.copy()
        request.POST['title']=request.POST['title'].lower()
        request.POST['title']=request.POST['title'].title()
        request.POST['content']=request.POST['content'].title()
        request.POST['written_by']=models.writer.objects.get(username=request.user.username)
        request.POST['slug']=slugify(request.POST['title'])
        form=forms.addblog(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bloggo')
    return render(request,'mainapp/create.html',context)

def error404(request):
    return render(request,'404.html')
