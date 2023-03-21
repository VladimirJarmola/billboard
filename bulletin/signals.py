from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Ans
from .tasks import send_notifications, send_response_condition


@receiver(post_save, sender=Ans)
def notify_about_new_ans(sender, instance, created, **kwargs):
    """Метод запускает функцию отправки сообщения автору объявления\
     по сигналу добавления отклика."""
    if created:
        send_notifications.apply_async(
            (instance.author.username, instance.text, instance.pk),
            countdawn=10,
            expires=120
        )


@receiver(post_save, sender=Ans)
def notify_about_ans_condition(sender, instance, update_fields, **kwargs):
    """Метод запускает функцию отправки сообщения автору отклика\
     по сигналу приятия отклика."""
    if instance.condition:
        send_response_condition.apply_async(
            (
                instance.author.username,
                instance.author.email,
                instance.text,
                instance.pk
            ),
            countdawn=10,
            expires=120
        )
