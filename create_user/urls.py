from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('registration/', views.Registration.as_view(), name='registration'),
    path('login/', views.NewLoginView.as_view(), name='login'),
    path('user_list/', views.UserListView.as_view(), name='user_list'),
]
