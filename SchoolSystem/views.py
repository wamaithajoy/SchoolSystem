from django.shortcuts import render,redirect

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







