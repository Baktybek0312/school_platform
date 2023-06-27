from django.db import models

from apps.lessons.models import LessonBlock, Lesson, HomeTask


class Courses(models.Model):
    title_of_courses = models.CharField(
        max_length=255,
        verbose_name='Название языка или продукта',
    )
    dates_of_the_event = models.DateTimeField(
        verbose_name='Даты проведения'
    )
    mentor_courses = models.CharField(
        max_length=255,
        verbose_name='Преподаватель'
    )
    sub_theme = models.ForeignKey(
        'SubTheme',
        on_delete=models.CASCADE,
        verbose_name='Подтемы',
        related_name='sub_theme_course',
    )

    course_completion_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Процент освоения темы'
    )

    def __str__(self):
        return self.title_of_courses

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class SubTheme(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Комментарий'
    )
    lesson_block = models.ForeignKey(
        LessonBlock,
        on_delete=models.CASCADE,
        verbose_name='Блок занятий',
        related_name='lesson_block_sub_theme'
    )
    list_of_lessons = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='list_lesson',
        verbose_name='Список уроков'
    )
    list_of_homework = models.ForeignKey(
        HomeTask,
        on_delete=models.CASCADE,
        verbose_name='Список ДЗ',
        related_name='list_homework'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подтема'
        verbose_name_plural = 'Подтемы'


class Exam(models.Model):
    date_exam = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата экзамена'
    )
    recommendations = models.TextField(
        blank=True,
        null=True,
        verbose_name='Общие рекомендации'
    )
    execution_time = models.DateTimeField(
        auto_created=True,
        verbose_name='Время выполнения'
    )
    lesson_block = models.ManyToManyField(
        to='lessons.LessonBlock',
        related_name='lesson_block_exam',
        verbose_name='Блокт занятий'
    )
    solved_task = models.TextField(
        blank=True,
        null=True,
        verbose_name='Решенное задание'
    )
    result = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Результаты'
    )

    def __str__(self):
        return self.recommendations

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Эказамены'
