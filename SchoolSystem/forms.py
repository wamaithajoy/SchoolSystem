from django import forms

from SchoolSystem.models import Staff, Student
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

    # firstname=forms.CharField(label="Enter first name",max_length=50,widget=forms.TextInput(attrs={'placeholder':'first name'}))
    # lastname=forms.CharField(label="Enter last name",max_length=50,widget=forms.TextInput(attrs={'placeholder':'last name'}))
    # email=forms.EmailField(label="Enter your email",max_length=40,widget=forms.TextInput(attrs={'placeholder':'email'}))
    # address=forms.CharField(label="Enter your address",max_length=30,widget=forms.TextInput(attrs={'placeholder':'address'}))
    # age=forms.IntegerField(label="Enter your age",widget=forms.TextInput(attrs={'placeholder':'age'}))
    # admissionNumber=forms.IntegerField(label="Enter your admission number",widget=forms.TextInput(attrs={'placeholder':'admission number'}))
    # phonenumber=forms.IntegerField(label="Enter your phone number",widget=forms.TextInput(attrs={'placeholder':'phone number'}))
    # emergencycontact=forms.IntegerField(label="Enter your emergency contact",widget=forms.TextInput(attrs={'placeholder':'emergencey contact'}))
    # GENDER=(('M','Male'),('F','Female'),('P','Prefer not to say'))
    # gender=forms.ChoiceField(label="Enter your gender", choices=GENDER)
    

   # firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Firstname', 'style': 'width: 300px;', 'class': 'form-control'}))
    #lastname = forms.CharField(widget=forms.EmailInput(attrs={'placeholder' :'Lastname', 'style': 'width: 300px;', 'class': 'form-control'}))
   # email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
   # address = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Address', 'style': 'width: 300px;', 'class': 'form-control'}))
    #age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder' :'Age', 'style': 'width: 300px;', 'class': 'form-control'}))
   # admissionNumber = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder' :'Admission Number', 'style': 'width: 300px;', 'class': 'form-control'}))
   # phonecontact = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder' :'Phone Contact', 'style': 'width: 300px;', 'class': 'form-control'}))
   # emergencyContact = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder' :'Emergency Contact', 'style': 'width: 300px;', 'class': 'form-control'}))

class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields="__all__"
   
    


    

    
