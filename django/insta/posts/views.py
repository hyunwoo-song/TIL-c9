from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
        
    else:
        post_form = PostForm()
    return render(request, 'posts/create.html', {'post_form':post_form})
    
    
    

