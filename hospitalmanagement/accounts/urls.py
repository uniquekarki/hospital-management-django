from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' ,  home  , name="home"),
    path('register' , register_attempt , name="register_attempt"),
    path('login' , login_attempt , name="login_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('logout', logout_attempt, name="logout_attempt"),
    path('schedule', schedule_appointments, name="schedule_appointments"),
    path('appointment', view_appointment, name='view_appointment'),
    path('delete/<id>', delete_appointment, name='delete_appointment'),
    path('update/<id>', update_appointment, name='update_appointment'),

]