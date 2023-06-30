from django.urls import path
from . import views
urlpatterns =[
path('home.html', views.home , name='home'),
path('courses.html', views.courses , name='courses'),
path('search', views.Search , name='search'),
#path('view.html', views.view , name='view'),
path('edit.html', views.edit , name='edit'),
path('newpage.html', views.newpage , name='newpage'),
path('signup.html', views.signup , name='signup'),
path('web.html', views.web , name='web'),
path('department.html', views.department , name='department'),
path('login.html', views.login , name='login'),
#path('about', views.about , name='index'),
]