from django.db import models
from django.contrib.auth.models import User


class RegisteredUser(models.Model):
    """
    Зарегестрированный юзер
    """
    # Юзер
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )
    # Отслеживаемые юзеры
    tracking = models.ManyToManyField(
        to='self',
        related_name='tracked_by',
        blank=True,
        symmetrical=False,
    )

    def __str__(self):
        return self.user.username


class Ownable(models.Model):
    """
    Абстрактная модель юзера владельца поста
    """
    user = models.ForeignKey(
        to='auth.User',
        on_delete=models.CASCADE,
        verbose_name="Author",
        related_name="%(class)ss",
    )

    class Meta:
        abstract = True


class FeedItem(Ownable):
    content = models.CharField(
        "Content",
        max_length=1000,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'
