from django.urls import path
from devapp import views

urlpatterns = [
    path('',views.index),
    path('book',views.books),
    path('book1',views.bookone),
     
]
