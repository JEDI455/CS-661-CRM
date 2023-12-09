from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete, LeadListView, LeadDetailView, LeadCreateView


app_name = "leads"

urlpatterns = [
    path ('', LeadListView.as_view(), name ='lead-list'),
    path ('create/', LeadCreateView.as_view(), name = 'lead-create'),
    path ('<int:pk>/', LeadDetailView.as_view(), name = 'lead-detail'),
    path ('<int:pk>/update/', lead_update, name ='lead-update'),
    path ('<int:pk>/delete/', lead_delete, name = 'lead-delete')
]
