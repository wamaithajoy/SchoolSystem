from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("teachersList/",views.teachers_list,name="teachersList"),
    path("studentsList",views.studentList,name="studentsList"),
    path('studentForm',views.StudentsForm,name="studentForm"),
    path('akirachix',views.akiraChix,name="akiraChix"),
    path('staffsList',views.staffList,name="staffsList"),
    path('staffForm',views.staffsForm,name="staffForm")

]

urlpatterns += staticfiles_urlpatterns()
