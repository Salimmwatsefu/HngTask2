from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.CreatePersonView.as_view(), name='person-create'),
    path('persons/<int:pk>', views.RetrieveUpdateDestroyPersonView.as_view(), name='person-detail')
]