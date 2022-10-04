from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [
    path("teachersList/",views.teachers_list,name="teachersList"),
    path("studentsList",views.studentList,name="studentsList"),
    path('studentForm',views.StudentsForm,name="studentForm"),
    path('akirachix',views.akiraChix,name="akiraChix"),
    path('staffsList',views.staffList,name="staffsList"),
    path('staffForm',views.staffsForm,name="staffForm"),
    path('student/<int:id>/',views.student_profile,name="student_profile"),
    path('ourteam',views.our_team,name="ourteam"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),

]

urlpatterns += staticfiles_urlpatterns()
