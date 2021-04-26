from django.urls import path

from mail_service import views

urlpatterns = [path("check/", views.DomainCheckAPI.as_view(), name="domain-check")]
