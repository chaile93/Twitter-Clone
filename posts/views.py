from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    
      #IF THE METHOD IS POST
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        
        #IF THE FORM IS VALID
        if form.is_valid(): 
           
        #THEN SAVE IT
         form.save()
        
        #THEN REDIRECT TO HOME
         return HttpResponseRedirect('/')
        
        #IF NO, GIVE ERROR MESSAGE
        else:
           return HttpResponseRedirect(form.erros.as_json())
        



 
# Get all posts, limit =20.
    posts = Post.objects.all().order_by('-created_at')[:20] #this "order_by post the most recent post at the top"
  
    return render(request, 'posts.html',
                  {'posts' : posts}
                  )    
    
# This is what will SHOW  on the web page

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')



def likes(request, post_id):
    heart = Post.objects.get(id = post_id)
    heart.like +=1
    heart.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = PostForm
    return render(request, 'edit.html', {'post': post, 'form': form})
    
    