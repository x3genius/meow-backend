from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
from .serializers import PetSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views import generic
from rest_framework.decorators import action
from rest_framework.response import Response
from random import sample


# Create your views here.
class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=["get"])
    def random(self, request):
        count = int(request.query_params.get("count", 4))

        pets = list(self.get_queryset())
        random_pets = sample(pets, min(count, len(pets)))

        serializer = self.get_serializer(random_pets, many=True)
        return Response(serializer.data)