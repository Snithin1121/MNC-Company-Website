from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
urlpatterns = [
    path('',views.base,name='base'),
    path('register/',views.register_user,name="register"),
    path('login/',auth_view.LoginView.as_view(template_name='Login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='Logout.html'),name='logout'),
    path('accounts/profile/',views.profile,name='profile'),
    path('Success/',views.Success,name="Success"),
    path('accounts/profile1/', views.profile1, name="profile1"),
    path('About/',views.About,name="About"),
    path('Contact/',views.Contact,name="Contact"),
    path('Contact1/',views.Contact1,name="Contact1"),
    path('About1/',views.About1,name="About1"),
]