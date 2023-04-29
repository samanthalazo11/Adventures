from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/' ,views.about, name='about'),
    path('destinations/', views.destinations_index, name='destinations_index'),
    path('destinations/<int:destination_id>/', views.destinations_detail, name='destinations_detail'),
    path('destinations/create/', views.DestinationCreate.as_view(), name='destinations_create'),
    path('destinations/<int:pk>/update/', views.DestinationUpdate.as_view(), name='destination_update'),
    path('destinations/<int:pk>/delete/', views.DestinationDelete.as_view(), name='destination_delete'),
    path('destinations/<int:destination_id>/add_restauraunts/', views.add_restauraunts, name='restauraunts'),
    path('destinations/<int:destination_id>/add_excursions/', views.add_excursions, name='excursions'),
    path('accounts/signup/', views.signup, name = 'signup')
    # path('destinations/<int:destination_id>/add_restauraunts/delete/', views.add_restaurauntsDelete.as_view(), name ='restauraunts_delete'),

]