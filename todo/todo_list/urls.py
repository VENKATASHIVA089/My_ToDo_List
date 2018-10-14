from django.urls import path
from . import views
from .models import User,List
urlpatterns = [
    path('<int:id>',views.home,name='home'),
    path('delete/<int:list_id>/',views.delete,name='delete'),
    path('cross_off/<int:list_id>/',views.cross_off,name='cross_off'),
    path('uncross/<int:list_id>/',views.uncross,name='uncross'),
    path('edit/<int:list_id>/',views.edit,name='edit'),
    path('login/',views.login,name='login'),
    path('create/',views.create,name='create'),
]
