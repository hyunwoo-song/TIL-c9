from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, ImageFormSet
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.db import transaction
# Create your views here.

def list(request):
    
    # posts= Post.objects.order_by('-id').all()
    # 1. 내가 follow하고 있는 사람들의 리스트
    followings = request.user.followings.all()
    # 2. 이 사람들이 작성한 Post들만 뽑아옴.
    posts = Post.objects.fitter(user__in=followings)
    comment_form = CommentForm()
    return render(request, 'posts/list.html', {'posts':posts, 'comment_form': comment_form })

@login_required
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        image_formset = ImageFormSet(request.POST, request.FILES)
        if post_form.is_valid() and image_formset.is_valid():
            post = post_form.save(commit=False)
            post.user=request.user
            
            with transaction.atomic():
                # 첫번째
                post.save() # 실제 데이터베이스에 저장
                # 두번째
                image_formset.instance = post
                image_formset.save() # 실제 데이터 베이스에 저장
            
            return redirect('posts:list')
        
    else:
        post_form = PostForm()
        image_formset = ImageFormSet()
    return render(request, 'posts/form.html', {'post_form':post_form, 'image_formset':image_formset})
    
def delete(request,post_id):
    # post= Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
        
    post.delete()
    return redirect('post:list')
    
@login_required    
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

@login_required
@require_POST
def comment_create(request, post_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment= comment_form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        commnet.save()
    return redirect('posts:list')

@require_http_methods(['GET','POST'])
def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return redirect('posts:list')
        
    comment.delete()
    return redirect('posts:list')
    

def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    
    return redirect('posts:list')
    



