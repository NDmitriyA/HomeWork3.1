from django.urls import path
from .views import MeasurementView_Create, SensorView, MeasurementView, SensorView_Update




urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
    path('sensor/<int:pk>/', SensorView_Update.as_view()),
    path('measurements/', MeasurementView_Create.as_view())
]