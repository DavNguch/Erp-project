from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup, name='signup'),
    #path('dashboard/',views.dashboard, name='dashboard'),
    path('wrong_login/',views.wrong_login, name='wrong_login'),
    path('logout/',views.logout, name='logout'),
    path('help/',views.help, name='help'),
    path('user_detail/',views.user_detail, name='user_detail'),

]