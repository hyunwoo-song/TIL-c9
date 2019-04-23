from django.shortcuts import render
from .forms import CrudForm

# Create your views here.
def create(request):
    crud_form = CrudForm()
    return render(request, 'crud/create.html', {'crud_form': crud_form})