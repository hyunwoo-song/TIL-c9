from django import forms
from .models import Crud

class CrudForm(forms.ModelForm): # form은 싱클를 맞추기 위해 쓴다.
    
    class Meta: # 데이터에 대한 데이터가 메타
        model = Crud
        fields = ['title']
        # 모든 fields 를 보여주고 싶을 때
        # fields = '__all__'