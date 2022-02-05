from django.urls import path
from demoapiapp import views

urlpatterns = [
    path('employees/',views.EmployeeListView.as_views())
]