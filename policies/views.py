from django.shortcuts import render
from rest_framework import serializers, generics
from .models import PolicyDetails
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

class PolicyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyDetails
        fields = "__all__"



class PolicyDetailsListView(generics.ListAPIView):
    queryset = PolicyDetails.objects.all()
    serializer_class = PolicyDetailsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'premium': ['gte', 'lte'],
        'coverage': ['gte'],
        'type':['exact']
    }

    search_fields=['name', 'type']
    ordering_fields = ['premium']
    ordering = ['premium']
