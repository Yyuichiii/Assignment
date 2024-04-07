from django.urls import path
from .views import UserRegistrationView,UserProfile,ReferralView,LoginView
urlpatterns = [
    
    path('register/',UserRegistrationView.as_view(),name='Register'),
    path('login/',LoginView.as_view(),name='Login'),
    path('profile/',UserProfile.as_view(),name='Profile'),
    path('referral/',ReferralView.as_view(),name='Referral'),
]