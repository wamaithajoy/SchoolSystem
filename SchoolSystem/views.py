from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from SchoolSystem.models import Staff, Student, Teacher
from SchoolSystem.forms import StaffForm, StudentForm

# Create your views here.
def teachers_list(request):
    teachers=Teacher.objects.all()
    return render(request,"teachersList.html",{"teachers":teachers})

def studentList(request):
    student=Student.objects.all()
    return render(request,"studentsList.html",{"students":student})

def StudentsForm(request):
    if request.method=="POST":

        student_form=StudentForm(request.POST,request.FILES)
        if student_form.is_valid():
            student_form.save()
            return redirect("studentsList")
        else:
            print(student_form.errors)
    else:
        student_form=StudentForm            

    return render(request,"studentForm.html",{'form':student_form})

def akiraChix(request):
    return render(request,"akirachix.html")

def staffList(request):
    staff=Staff.objects.all()
    return render(request,"staffList.html",{"staffs":staff})   

def staffsForm(request):
    if request.method=="POST":

        staff_form=StaffForm(request.POST,request.FILES)
        if staff_form.is_valid():
            staff_form.save()
            return redirect("staffsList")
        else:
            print(staff_form.errors)
    else:
        staff_form=StaffForm

    return render(request,"staffForm.html",{'form':staff_form})  

def student_profile(request,id):
    student=Student.objects.get(id=id)
    return render(request,"student_profile.html",{"student":student}) 

def our_team(request):
    return render(request,"team.html") 

@login_required
def home(request):
    return render(request, "akirachix.html", {})
 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('akirachix')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})   



            






