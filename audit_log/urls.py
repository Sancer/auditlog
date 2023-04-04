from django.urls import path

from .views import ListLogView, V2ListLogView

app_name = 'audit_log'
urlpatterns = [
    path('v1/log/', ListLogView.as_view(), name='v1_list_log'),  # usando directamente la DB
    path('v2/log/', V2ListLogView.as_view(), name='v2_list_log'), # usando el repository para simular que usa otra persistencia
]
