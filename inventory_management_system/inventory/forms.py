from django import forms
from .models import *

class DBMSForm(forms.ModelForm):
    class Meta:
        model = DBMS
        fields = ('MidSem', 'EndSem', 'Attendance', 'Others')


class DAAForm(forms.ModelForm):
    class Meta:
        model = DAA
        fields = ('MidSem', 'EndSem', 'Attendance', 'Others')
        

class DSForm(forms.ModelForm):
    class Meta:
        model = DS
        fields = ('MidSem', 'EndSem', 'Attendance', 'Others')
