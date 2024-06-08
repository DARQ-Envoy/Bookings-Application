from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Booking, Table


@receiver(post_save,sender = Booking)
def update_isbooked_table_attr_oncreate(sender,instance,created,**kwargs):
    if created:
        table = instance.table
        table.is_booked = True
        table.save()

@receiver(post_delete, sender= Booking)
def update_table_isbooked_attr_ondelete(sender,instance, created, **kwargs):
    table = instance.table
    table.is_booked = False
    table.save()


