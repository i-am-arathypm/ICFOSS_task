from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('password/',views.change_password,name='password'),
    # path('edit/<int:b_id>',views.edit,name='edit'),
    # path('delete/<int:b_id>',views.delete,name='delete')
]