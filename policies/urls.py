from django.urls import path
from .views import PolicyDetailsListView

urlpatterns = [
    path('policies/', PolicyDetailsListView.as_view(), name='policy-list')
]