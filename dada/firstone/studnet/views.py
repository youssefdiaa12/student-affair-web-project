from genericpath import exists
from django.shortcuts import render
from .models import studnet
from django.template import loader
from django.contrib import messages
# Create your views here.
def studnet_inf(request):
   return render(request, 'pages/html/view.html',{'students':studnet.objects.all()})
def search(request):
    title=request.GET['searched']
    searching=studnet.objects.filter(student_id__contains=title)
    context={
    'search' : searching,
    }
    return render(request, 'pages/html/views.html',context)
def courses(request):
    title=request.GET['id']
    if studnet.objects.filter(student_id=title).exists():
     temp=studnet.objects.get(student_id=title)
     title2=request.GET['name']
     if studnet.objects.filter(course__contains=title2).exists():
      messages.error(request,"THE COURSE IS AlREADY EXISTED")
      return render(request, 'pages/html/courses.html') 
     else:
      temp.course=temp.course+','+title2
      title3=request.GET['sbaey']
      temp.department=title3
      temp.save(update_fields=['course','department'])
      return render(request, 'pages/html/courses.html')    
    else:
     messages.error(request,"THE ID IS NOT EXISTED")
     return render(request, 'pages/html/courses.html')  
def department(request):
    title=request.GET['id']
    if studnet.objects.filter(student_id=title).exists():
     temp=studnet.objects.get(student_id=title)
     title2=request.GET['depart']
     temp.department=title2
     temp.save(update_fields=['department'])
     return render(request, 'pages/html/department.html')    
    else:
     messages.error(request,"THE ID IS NOT EXISTED")
     return render(request, 'pages/html/department.html')  
def signup(request):
  q = studnet(
  studentname=request.GET['name'],
  course=request.GET['name1'],
  department=request.GET['lol'],
  student_id=request.GET['id'],
  gender=request.GET['gender'],
  email=request.GET['mail'],
  mob=request.GET['no'],
  password=request.GET['pass'],
  gpa=request.GET['gpa'],
  activation=request.GET['lol1'])
  q.save() 
  return render(request, 'pages/html/signup.html')    
def edit(request):
 title=request.GET['id1']
 if studnet.objects.filter(student_id=title).exists():
  temp1=studnet.objects.get(student_id=title)
  temp1.studentname=request.GET['name']
  temp1.course=request.GET['name1']
  temp1.department=request.GET['lol']
  temp1.gender=request.GET['gender']
  temp1.email=request.GET['mail']
  temp1.mob=request.GET['no']
  temp1.password=request.GET['pass']
  temp1.gpa=request.GET['gpa']
  temp1.activation=request.GET['lol1']
  temp1.save(update_fields=['studentname','course','department','gender','email','mob','password','gpa','activation'])
  return render(request,'pages/html/edit.html') 
 else:
     messages.error(request,"THE ID IS NOT EXISTED")
     return render(request, 'pages/html/edit.html') 
def login(request):
 title=request.GET.get('id',None)
 if studnet.objects.filter(student_id=title).exists():
    temp=studnet.objects.get(student_id=title)
    title2=request.GET['id1']
    if temp.password==title2:
      return render(request,'pages/html/home.html') 
    else:
       messages.error(request,"THE PASSWORD IS NOT EXISTED")
       return render(request, 'pages/html/login.html') 
 else:
    messages.error(request,"THE ID IS NOT EXISTED")
    return render(request, 'pages/html/login.html') 


