from django.shortcuts import render
from .models import Student

# Create your views here.

def new(request):
    return render(request, 'new.html')

def create(request):
    name = request.GET.get('name') 
    email = request.GET.get('email')
    birthday = request.GET.get('birthday')
    age = request.GET.get('age')
    
    student = Student(name=name, email=email, birthday=birthday, age=age)
    student.save() 
    
    return render(request, 'create.html')

def index(request):
    students = Student.objects.all()
    
    return render(request, 'index.html', {'students':students})
