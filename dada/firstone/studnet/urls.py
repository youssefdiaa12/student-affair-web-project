from django.urls import path
from . import views

urlpatterns=[
    path('view',views.studnet_inf,name='studnet_inf'),
    path('views',views.search,name='search_student'),
    path('addcourse',views.courses,name='course_student'),
    path('adddepart',views.department,name='depart_student'),
    path('addstudent',views.signup,name='add_student'),
    path('editstudent',views.edit,name='edit_student'),
    path('',views.login,name='login_student'),
    ]