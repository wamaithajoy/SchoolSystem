from django.urls import path
from . import views

urlpatterns = [
    path("teachersList/",views.teachers_list,name="teachersList"),
]
