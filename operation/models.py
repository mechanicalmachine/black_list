from django.contrib.auth.models import User
from django.db import models


STATUS_CHOICES = (
    ('a', 'В черном списке'),
    ('n', 'Не в черном списке')
)


class BlackList(models.Model):
    value = models.CharField(
        max_length=20,
        blank=False,
        verbose_name='Номер телефона'
    )
    added_date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        editable=False,
        verbose_name='Дата добавления'
    )
    reason = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='Причина добавления'
    )
    added_by = models.ForeignKey(
        User,
        null=False,
        blank=True,
        editable=False,
        on_delete=models.PROTECT,
        verbose_name='Кем добавлено'
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        verbose_name='Статус'
    )
