from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list", views.list, name="list"),
    path("list/<get_vegetable>", views.get_vegetable, name="get_vegetable"),
    path("forecast", views.forecast, name="forecast"),
    path("todays-tasks", views.todays_tasks, name="todays-tasks"),
]
