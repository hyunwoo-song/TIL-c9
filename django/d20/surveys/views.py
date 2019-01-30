from django.shortcuts import render, redirect
from .models import Question, Choice

# Create your views here.
def new(request):
    return render(request, 'new.html')


def create(request):
    title = request.POST.get('title')  # POST는 요청 방식
    question = Question(title=title)
    question.save()
    return redirect('surveys:detail', question.pk)
    

def detail(request, question_id):    
    question = Question.objects.get(pk=question_id) #id도 그냥 이름이다
    return render(request, 'detail.html', {'question':question})
    
def index(request):
    question = Question.objects.all()
    return render(request, 'index.html', {'question':question})
    
def delete(request, question_id):
    # 삭제하는 코드
    question = Question.objects.get(pk=question_id)
    question.delete()
    return redirect("surveys:list")
    
def edit(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'edit.html', {'question':question})

def update(request, question_id):
    # 수정하는 코드
    question = Question.objects.get(pk=question_id)
    question.title = request.POST.get('title')
    question.save()
    return redirect('surveys:detail', question.pk)

def choice_create(request, question_id):
    # 댓글을 달 게시물
    question = Question.objects.get(pk=question_id)
    
    # form에서 넘어온 댓글 내용
    content = request.POST.get('content')
    votes = request.POST.get('votes')
    
    # 댓글 생성 및 저장
    choice = Choice(question=question, content=content, votes= votes)
    choice.save()
    return redirect('surveys:detail', question.pk)
    
def choice_delete(request, question_id, choice_id):
    choice = Choice.objects.get(pk=choice_id)
    choice.delete()
    return redirect('surveys:detail', question_id)
    
    