from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.ListCreatePersonView.as_view(), name='person-list-create'),
    path('persons/<int:pk>', views.RetrieveUpdateDestroyPersonView.as_view(), name='person-detail')
]