from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from .models import Post
from .forms import PostModelForm,PostForm
from django.views.generic.edit import CreateView
from django.http import HttpResponse

# Create your views here.


def index(request):
    obj=Post.objects.all()
    return render(request,'index.html',{'obj':obj})


def upload(request):
    form=PostModelForm(request.POST,request.FILES)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        form=PostModelForm()
    template_name='form.html'
    context={'form':form}
    return render(request,template_name,context)
    
        
  



def update_post(request,id):
   
    
    blogger_sel=Post.objects.get(id=id)
    form = PostModelForm(request.POST,instance=blogger_sel)
    if form.is_valid():
        form.save()
        
    return render(request,'form.html',{'form':form})


def delete_post(request,id):
    blogger_sel=get_object_or_404(Post,id=id)
    if request.method=="POST":
        blogger_sel.delete()
       
    return render(request,'delete.html',{"object":blogger_sel})



def post_list(request):
    
    qs=Post.objects.all()
    template_name= 'home.html'
    context= {'object_list':qs}
    return render(request,template_name,context)


def post_detail(request,id):
    obj=get_object_or_404(Post,id=id)
    template_name= 'detail.html'
    context= {"object":obj}
    return render(request,template_name,context)

   

    
   







        
