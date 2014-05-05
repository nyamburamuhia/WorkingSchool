from django.http import HttpResponse,HttpRequest
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from passlib.hash import sha256_crypt
from django.contrib.auth import authenticate, login, logout
from classes.models import Class
from students.models import Student

@csrf_exempt
def login_student_form(request):
    return render_to_response('students/login.html', {})


def register_student(request):
    "return register teacher template"    
    context={}
    classes=list(Class.objects.all())
    context['classes']=classes
    return render_to_response('students/register.html', context)

@csrf_exempt
def register_student_add(request):
    if request.method=="POST":        
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        gender=request.POST['gender']
        username=request.POST['username']
        password=request.POST['password']
        class_id=request.POST['class_id']
        
        # hash the password
        hashed_password = sha256_crypt.encrypt(password)
        
        student=Student(first_name=first_name,last_name=last_name,gender=gender,username=username,password=hashed_password,classid_id=class_id)
        student.save()
        
        return login_student_form(request)
    
@csrf_exempt
def login_student(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        # hash the password
        #hashed_password = sha256_crypt.encrypt(password)
        
        #select user from database
        student=Student.objects.get(username=username)
        
        context={}
        context['student']=student
        context['class_id']=student.classid
        
        return render_to_response("students/home.html",context)
    
def list_students(request):
    #students_list=list(Student.objects.all())
    students_list=Student.objects.all()
    context={}
    context['students_list']=students_list
    return render_to_response("students/list_students.html",context)

def delete_student(request,student_id):
    student=Student.objects.get(student_id=student_id)
    student_first_name=student.first_name
    student_last_name=student.last_name
    
    student.delete()
    return HttpResponse(student_first_name+" "+student_last_name+ " has been deleted successfully")
    

def edit_student_form(request,student_id):  
    student=Student.objects.get(student_id=student_id)
    classes=Class.objects.all()
    context={}
    context['student']=student  
    context['classid']=student.classid
    context['classes']=classes
    return render_to_response("students/edit_student.html",context)

@csrf_exempt
def edit_student(request,student_id):    
    student=Student.objects.get(student_id=student_id)
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        gender=request.POST['gender']
        class_id=request.POST['class_id']
        
        if student.first_name!=first_name:
            student.first_name=first_name
            student.save()
        if student.last_name!=last_name:
            student.last_name=last_name
            student.save()
        if student.gender!=gender:
            student.gender=gender
            student.save()
        if student.classid_id!=class_id:
            student.classid_id=class_id
            student.save()
    return redirect("/student/edit/"+student_id+"/",{})
        