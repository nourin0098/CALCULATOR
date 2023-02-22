from django.urls import path
from calc import views

urlpatterns =[
    path('',views.home),
    path('calc/',views.calc,name='calculation'),
    

]
