from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class CreatePersonView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class RetrieveUpdateDestroyPersonView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'pk'
