from django.db import models


class LessonBlock(models.Model):
    number = models.IntegerField(
        unique=True,
        verbose_name='Номер',
    )
    name_block = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    goal_at_the_end = models.TextField(
        blank=True,
        null=True,
        verbose_name='цель по окончании'
    )

    def __str__(self):
        return self.name_block

    class Meta:
        verbose_name = 'Блок занятия'
        verbose_name_plural = 'Блок занятий'


class Lesson(models.Model):
    motivation = models.TextField(
        blank=True,
        null=True,
        verbose_name='Мотивация',
    )
    updating = models.ForeignKey(
        'Updating',
        on_delete=models.CASCADE,
        related_name='lesson_updating',
    )
    new_topic = models.ForeignKey(
        'NewTopic',
        on_delete=models.CASCADE,
        related_name='lesson_new_topic',
        verbose_name='Новая тема'
    )
    reflection = models.ForeignKey(
        'Reflection',
        on_delete=models.CASCADE,
        related_name='reflection_lesson'
    )
    comments = models.TextField(
        blank=True,
        null=True,
        verbose_name='Комментарии'
    )
    date_lesson = models.DateField(
        auto_now=True,
        verbose_name='дата'
    )
    group = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name='группа'
    )
    lesson_block = models.ForeignKey(
        LessonBlock,
        on_delete=models.CASCADE,
        verbose_name='Блок занятий',
        related_name='lesson_block_lesson'
    )

    def __str__(self):
        return self.motivation

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Updating(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='содержит название',

    )
    practical_exercises = models.TextField(
        blank=True,
        null=True,
        verbose_name='практические упражнения'
    )

    def __str__(self):
        return self.name


class NewTopic(models.Model):
    name = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name='название'
    )
    material = models.TextField(
        blank=True,
        null=True,
        verbose_name='материал'
    )
    practical_exercises = models.TextField(
        blank=True,
        null=True,
        verbose_name='практические упражнения'
    )

    def __str__(self):
        return self.name


class Reflection(models.Model):
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name='текст'
    )
    feedback = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name='обратной связи'
    )


class Glossary(models.Model):
    terms_block = models.ForeignKey(
        'TermsBlock',
        on_delete=models.PROTECT,
        related_name='terms_blocks',
        verbose_name='Блок терминов'
    )
    term = models.TextField(
        blank=True,
        null=True,
        verbose_name='Термин'
    )
    definition = models.TextField(
        blank=True,
        null=True,
        verbose_name='Определение'
    )
    using = models.TextField(
        blank=True,
        null=True,
        verbose_name='Использование'
    )
    lesson_url = models.ForeignKey(
        Lesson,
        on_delete=models.PROTECT,
        related_name='lesson_url_data'
    )
    sub_theme = models.ForeignKey(
        to='courses.SubTheme',
        on_delete=models.PROTECT,
        related_name='sub_theme_glossary'
    )


class TermsBlock(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='название'
    )


class HomeTask(models.Model):
    date_lesson_task = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.PROTECT,
        related_name='lesson_home_task',
    )
    topic = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Темы'
    )
    task = models.TextField(
        blank=True,
        null=True,
        verbose_name='Задание'
    )

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашнее задание'
