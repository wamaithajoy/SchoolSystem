

























from django.db import models
from django.utils import timezone

# Create your models here.

class School(models.Model):
    school_name=models.CharField(max_length=20,null=True)
    school_address=models.TextField(null=True)
    school_email=models.EmailField(max_length=20,null=True)
    location=models.CharField(null=True,max_length=15)
    contact=models.IntegerField(null=True)

class Student(models.Model):
    first_name=models.CharField(max_length=15,null=True)  
    last_name=models.CharField(max_length=15,null=True)
    my_email=models.EmailField(max_length=20,null=True)
    GENDER_CHOICES=(
        ("Female","Female"),("Male","Male"),("Prefer not to say","Prefer not to say")
    )
    my_gender=models.CharField(max_length=17,null=True,choices=GENDER_CHOICES)
    myaddress=models.CharField(null=True,max_length=17)
    STREAM_CHOICES=(
        ("Adalab","Adalab"),("Annita B","Annita B"),("Hopper Lab","Hopper Lab")
    )
    my_stream=models.CharField(max_length=15,null=True,choices=STREAM_CHOICES)
    # age=models.PositiveSmallIntegerField(null=True)
    # admission_number=models.IntegerField(null=True)
    my_contact=models.IntegerField(null=True)
    NATIONALITY={
        ("Kenya","Kenya"),("Tanzania","Tanzania"),("Uganda","Uganda"),("Rwanda","Rwanda"),
        ("South Sudan","South Sudan")
    }
    nationality=models.CharField(max_length=30,null=True,choices=NATIONALITY)

    # emergency_contact=models.IntegerField(null=True)
    profile=models.ImageField

class StudentId(models.Model):
    student=models.ForeignKey('Student',null=True,on_delete=models.CASCADE,related_name="StudentId_Student")  
    date_issued=models.DateField(default=timezone.now)
    expiry_date=models.DateField(default=timezone.now)
    profile_picture=models.ImageField

class Teacher(models.Model):
    firstname=models.CharField(max_length=15,null=True)
    lastname=models.CharField(max_length=15,null=True) 
    UNIT_CHOICES=(
        ("Python","Python"),("Kotlin","Kotlin"),("FR","Frontendweb"),
        ("IOT","IOT"),("Research","UserResearch"),
        ("Design","UI/UX Design"),("PD","Professiondevelopment"),
        ("NYJ","Navigating Your Journey")
    )
    unit_specialty=models.CharField(max_length=11,null=True,choices=UNIT_CHOICES)
    contact=models.IntegerField(null=True)
    email=models.EmailField(max_length=20,null=True)
    profile_picture=models.ImageField
    school=models.ForeignKey('School',null=True,on_delete=models.CASCADE,related_name="Teacher_School")

class SchoolFees(models.Model):
    student=models.ForeignKey('Student',null=True,on_delete=models.CASCADE,related_name="SchoolFees_Student")
    full_fees=models.IntegerField(null=True)
    amount_paid=models.IntegerField(null=True)
    balance=models.IntegerField(null=True)
    receipt=models.ForeignKey('Receipt',null=True,on_delete=models.CASCADE,related_name="SchoolFees_Receipt")

class Receipt(models.Model):
    student=models.ForeignKey('Student',null=True,on_delete=models.CASCADE,related_name="Receipt_Student")
    school_account=models.ForeignKey('SchoolAccount',null=True,on_delete=models.CASCADE,related_name="Receipt_SchoolAccount")
    amount_paid=models.IntegerField(null=True)
    balance=models.IntegerField(null=True)
    receipt_number=models.IntegerField(null=True)

class SchoolAccount(models.Model):
    school=models.ForeignKey('School',null=True,on_delete=models.CASCADE,related_name="SchoolAccount_School")
    account_name=models.CharField(max_length=25,null=True)
    account_number=models.IntegerField(null=True)

class Staff(models.Model):
    firstname=models.CharField(max_length=30,null=True)
    lastname=models.CharField(max_length=30,null=True) 
    OCCUPATION_CHOICES=(
        ("Chef","Chef"),("Cook","Cook"),("Gate keeper","Gate Keeper"),
        ("Gardener","Gardener"),("Matron","Matron"),
        ("Accountant","Accountant"),("Nurse","Nurse"),
        ("CodeHive Lead","CodeHive Lead")
    )
    specialtys=models.CharField(max_length=22,null=True,choices=OCCUPATION_CHOICES)
    Mycontact=models.IntegerField(null=True)
    My_email=models.EmailField(max_length=40,null=True)
    profile_picture=models.ImageField
    # My_school=models.ForeignKey('School',null=True,on_delete=models.CASCADE,related_name="Staff_School")
    GENDER=(
        ("Male","Male"),("Female","Female"),("Prefer not to say","Prefer not to say")
    )
    Mygender=models.CharField(max_length=17,null=True,choices=GENDER)
    WORK_PERIOD=(
        ("1 Year","1 Year"),("2 Years","2 Years"),("3 Years","3 Years"),
        ("4 Years","4 Years"),("5 Years","5 Years")
    )
    Duration=models.CharField(max_length=22,null=True,choices=WORK_PERIOD)

class AcademicAnalysis(models.Model) :
     student=models.ForeignKey('Student',null=True,on_delete=models.CASCADE,related_name="AcademicAnalysis_Student")
     GRADE_CHOICES=(
      ("A","A"),("A-","A-"),("B+","B+"),
        ("B","B"),("B-","B-"),
        ("C+","C+"),("C","C"),
        ("C-","C-")  
     )
     grade=models.CharField(max_length=5,null=True,choices=GRADE_CHOICES)

class LibraryManagement(models.Model):
    student=models.ForeignKey('Student',null=True,on_delete=models.CASCADE,related_name="LibraryManagement_Student")
    date_issued=models.DateTimeField(default=timezone.now)
    return_date=models.DateTimeField(default=timezone.now)






    


    




