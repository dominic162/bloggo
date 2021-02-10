from django.urls import path
from auth import views

urlpatterns = [
    path('login',views.auth_login,name="auth_login"),
    path('logout',views.auth_logout,name="auth_logout"),
    path('signup',views.auth_signup,name="auth_signup")
]