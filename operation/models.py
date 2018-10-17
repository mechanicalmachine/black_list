from django.db import models


class BlackList(models.Model):
    value = models.CharField(
        max_length=20,
        verbose_name='Номер телефона'
    )
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    added_date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        editable=False
    )
