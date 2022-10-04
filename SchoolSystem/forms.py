from django import forms
from SchoolSystem.models import Staff, Student
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields="__all__"

   
    


    

    
