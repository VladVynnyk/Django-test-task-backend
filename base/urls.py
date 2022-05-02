from django.urls import path
from . import views
urlpatterns = [
    #Read the data
    path('users/all-users', views.getUsers, name="getUsers"),
    path('groups/all-groups', views.getGroups, name="getGroups"),
    #Create the data
    path('users/add-user', views.addUser, name="addUser"),
    path('groups/add-group', views.addGroup, name="addGroup"),
    #Update the data
    path('users/edit-user/<str:pk>/', views.editUser, name="editUser"),
    path('groups/edit-group/<str:pk>/', views.editGroup, name="editGroup"),
    #Delete the data
    path('users/delete-user/<str:pk>/', views.deleteUser, name="deleteUser"),
    path('groups/delete-group/<str:pk>/', views.deleteGroup, name="deleteGroup"),
    #Filter the data
    path('filter/', views.filterData, name='filter'),
]

