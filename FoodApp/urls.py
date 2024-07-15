from . import views
from django.contrib import admin
from django.urls import path

app_name='FoodApp'

urlpatterns=[
    #/food/
    path('',views.IndexClassView.as_view(),name='index'),
    #/food/
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('item/',views.item,name='item'),
    #/add items/
    path('add',views.CreateItem.as_view(),name='create_item'),
    #edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]