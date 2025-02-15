from django.urls import path
from .views import (
    login_admin,
    get_viajes_pasajero,
    get_viaje_pasajero_by_id,
    get_vehiculos,
    get_vehiculo_by_id,
    create_vehiculo,
    update_vehiculo,
    delete_vehiculo
)

urlpatterns = [
    path('login/admin/', login_admin, name='login_admin'),
    path('viajes_pasajero/', get_viajes_pasajero, name='get_viajes_pasajero'),
    path('viajes_pasajero/<int:id>/', get_viaje_pasajero_by_id, name='get_viaje_pasajero_by_id'),
    path('vehiculos/', get_vehiculos, name='get_vehiculos'),
    path('vehiculos/<int:id>/', get_vehiculo_by_id, name='get_vehiculo_by_id'),
    path('vehiculos/create/', create_vehiculo, name='create_vehiculo'),
    path('vehiculos/update/<int:id>/', update_vehiculo, name='update_vehiculo'),
    path('vehiculos/delete/<int:id>/', delete_vehiculo, name='delete_vehiculo'),
]