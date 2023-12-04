from django.urls import path, include
from .views import lead_list

app_name = "leads"

urlpatterns = [
    path ('', lead_list),
]
