from django.shortcuts import render
from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import DragandDrop, Draggable, AddingColor
from . import serializers


class AddColorViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = AddingColor.objects.all()
    serializer_class = serializers.AddingColorSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ['draganddrop']


class DragandDropViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = DragandDrop.objects.all()
    serializer_class = serializers.DragandDropSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ['draggable']


class DragandDropListViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = DragandDrop.objects.all()
    serializer_class = serializers.DragandDropListSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ['draggable']


class DraggableViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Draggable.objects.all()
    serializer_class = serializers.DraggableSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    search_fields = ['name']
    # filter_fields = ['']


class DraggableListViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Draggable.objects.all()
    serializer_class = serializers.DraggableListSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    search_fields = ['name']
    filter_fields = ['drag_of_draggable']

    def get_serializer_class(self):
        serializer_class = serializers.DraggableListSerializer
        if self.action in ['create', 'update', 'partial_update']:
            serializer_class = serializers.DraggableListSerializer
        return serializer_class