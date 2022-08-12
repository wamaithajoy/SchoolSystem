from django.shortcuts import render

from SchoolSystem.models import Teacher

# Create your views here.
def teachers_list(request):
    teachers=Teacher.objects.all()
    return render(request,"teachersList.html",{"teachers":teachers})

