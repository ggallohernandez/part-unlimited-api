from django.db import connection
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from parts.models import Part


@receiver(post_save, sender=Part)
def refresh_materialized_view(sender, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute("REFRESH MATERIALIZED VIEW parts_description_top_5_words")
