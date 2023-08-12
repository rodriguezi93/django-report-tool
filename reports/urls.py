from django.urls import path

from . import views

urlpatterns = [
    path("newreport", views.newreport),
    path("savedreports",views.savedreports)
]