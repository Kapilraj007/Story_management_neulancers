from django.urls import path
from . import views

urlpatterns = [
    path('register_login',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('profile/<str:id>/',views.profile,name="profile"),
    path('updateprofile/<str:id>/',views.updateProfile,name="updateprofile")
]