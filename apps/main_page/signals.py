import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.conf import settings
from django.db.models import ImageField
from django.apps import apps

def convert_image_field(instance, field):
    if 'icon' in field.name:
        return

    image_field = getattr(instance, field.name)

    if image_field:
        image_path = image_field.path
        webp_path = os.path.splitext(image_path)[0] + '.webp'

        try:
            with Image.open(image_path) as img:
                img.save(webp_path, 'webp')

            os.remove(image_path)
            setattr(instance, field.name, os.path.relpath(webp_path, settings.MEDIA_ROOT))
            instance.save()

        except Exception as e:
            print(f"Error processing image for model {instance.__class__.__name__}, field {field.name}: {e}")

def convert_to_webp(instance):
    for field in instance._meta.fields:
        if isinstance(field, ImageField):
            convert_image_field(instance, field)

@receiver(post_save)
def post_save_handler(sender, instance, **kwargs):
    if hasattr(instance, '_meta') and any(isinstance(field, ImageField) for field in instance._meta.fields):
        convert_to_webp(instance)

def register_signals():
    for model in apps.get_models():
        post_save.connect(post_save_handler, sender=model)


