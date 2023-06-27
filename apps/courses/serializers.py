from rest_framework import serializers

from apps.courses.models import (
    Courses, SubTheme
)


class SubThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTheme
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    sub_theme_course = SubThemeSerializer(many=True, read_only=True)

    class Meta:
        model = Courses
        fields = '__all__'
