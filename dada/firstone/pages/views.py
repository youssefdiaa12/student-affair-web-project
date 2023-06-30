from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'pages/html/home.html')
def edit(request):
    return render(request, 'pages/html/edit.html')
def web(request):
    return render(request, 'pages/html/web.html')
def newpage(request):
    return render(request, 'pages/html/newpage.html')
def courses(request):
    return render(request, 'pages/html/courses.html')
def department(request):
    return render(request, 'pages/html/department.html')
def signup(request):
    return render(request, 'pages/html/signup.html')
def Search(request):
    return render(request, 'pages/html/search.html')
def login(request):
    return render(request, 'pages/html/login.html')

