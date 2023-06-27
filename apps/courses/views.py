from rest_framework import (
    generics, viewsets, views
)

from apps.courses.models import Courses
from apps.courses.serializers import CoursesSerializer


class CoursesAPIView(generics.ListCreateAPIView):
    """Class for create and list courses"""
    serializer_class = CoursesSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Courses.objects.all()


class CoursesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Class for retrieve, udpate and delete courses"""
    serializer_class = CoursesSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Courses.objects.all()
