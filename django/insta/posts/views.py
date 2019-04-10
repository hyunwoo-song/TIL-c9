from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def list(request):
    posts= Post.objects.order_by('-id').all()
    return render(request, 'posts/list.html', {'posts':posts})

@login_required
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user=request.user
            post_form.save()
            return redirect('posts:list')
        
    else:
        post_form = PostForm()
    return render(request, 'posts/form.html', {'post_form':post_form})
    
def delete(request,post_id):
    # post= Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
        
    post.delete()
    return redirect('post:list')
    
    
def update(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    return render(request, 'posts/form.html', {'post_form':post_form})
    
    
    

