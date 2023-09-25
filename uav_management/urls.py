from django.urls import path
from . import views

urlpatterns = [
    # path("", views.UAVList, name= "uav_list"),
    path("uav_create/", views.UAVCreate, name= "uav_create"),
    path("uav_create_api/", views.UAVCreateApi, name= "uav_create_api"),


    path("uav_update/<str:pk>/", views.UAVUpdate, name= "uav_update"),
    path("uav_delete/<str:pk>/", views.UAVDelete, name= "uav_delete"),
    path('rental/<str:pk>/', views.rental_list, name='rental_list'),
    path('retnal_create/<str:pk>/', views.create_rental, name='create_rental'),

    path('rental_list_user/', views.rental_list_user, name='rental_list_user'),
    path('rental_update/<int:pk>/', views.update_rental, name='update_rental'),
    path("rental_delete/<int:pk>/", views.delete_rental, name="delete_rental"),


]
