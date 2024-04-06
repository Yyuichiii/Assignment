from django.urls import path
from .views import UserRegistrationView
urlpatterns = [
    
    path('register/',UserRegistrationView.as_view(),name='Register'),
#     path('login/',LoginView.as_view(),name='Login'),
#     path('profile/',UserProfile.as_view(),name='Profile'),
#     path('password/',passchange.as_view(),name='Password'),
#     path('sendEmail/',emailview.as_view(),name='Send_Email'),
#     path('reset/<uid>/<token>/',reset_password_view.as_view(),name='Password_Change'),
]