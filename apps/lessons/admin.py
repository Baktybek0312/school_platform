from django.contrib import admin

from apps.lessons.models import *


@admin.register(LessonBlock)
class LessonBlockAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'number',
        'name_block', 'goal_at_the_end'
    )


@admin.register(Updating)
class UpdatingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'practical_exercises'
    )
    list_display_links = (
        'name',
    )


@admin.register(NewTopic)
class NewTopicAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
        'material', 'practical_exercises'
    )
    list_display_links = (
        'name',
    )


@admin.register(Reflection)
class ReflectionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'text',
        'feedback'
    )
    list_display_links = (
        'text',
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'motivation', 'updating',
        'new_topic', 'reflection', 'comments',
        'date_lesson', 'group',
    )
    list_display_links = (
        'motivation',
    )


@admin.register(HomeTask)
class HomeTaskAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'date_lesson_task',
        'lesson', 'topic', 'task',
    )



