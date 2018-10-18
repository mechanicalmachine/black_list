from django.contrib.auth.models import User
from django.db import models


STATUS_CHOICES = (
    (True, 'В черном списке'),
    (False, 'Не в черном списке')
)


class PhonesList(models.Model):
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
        related_name='who_added',
        on_delete=models.PROTECT,
        verbose_name='Кем добавлено'
    )
    status = models.BooleanField(
        editable=False,
        choices=STATUS_CHOICES,
        verbose_name='Статус'
    )
    excluded_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        editable=False,
        related_name='who_removed',
        on_delete=models.PROTECT,
        verbose_name='Кем удалено'
    )
    excluded_date = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name='Дата удаления'
    )
