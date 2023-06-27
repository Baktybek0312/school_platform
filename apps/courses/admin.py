from django.contrib import admin

from apps.courses.models import SubTheme, Courses


@admin.register(SubTheme)
class SubThemeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
        'description',
        'lesson_block',
    )
    list_display_links = (
        'id', 'name'
    )


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title_of_courses', 'dates_of_the_event',
        'mentor_courses', 'sub_theme', 'course_completion_rate',
    )
    list_display_links = (
        'id', 'title_of_courses'
    )
