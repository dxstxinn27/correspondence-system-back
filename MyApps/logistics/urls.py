"""
Envolviendo Vistas de Api
"""

from django.urls import path

from MyApps.logistics.views import transport_list, transport_detail, service_list, service_detail, route_list, route_detail


urlpatterns = [
    path('transport/', transport_list, name='transport_list'),
    path('transport/<int:pk>/', transport_detail, name='transport_detail'),
    path('service/', service_list, name='service_list'),
    path('service/<int:pk>/', service_detail, name='service_detail'),
    path('route/', route_list, name='route_list'),
    path('route/<int:pk>/', route_detail, name='route_detail'),
]
