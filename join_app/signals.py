from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import User

@receiver(pre_delete, sender=User)
def delete_user_related_objects(sender, instance, **kwargs):
    instance.tasks.all().delete()
    instance.contacts.all().delete()
