from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('## Pre Save Signal ##')
    print(f'Instance: {instance}')
    print(f'Sender: {sender}')
    print(f'Kwargs: {kwargs}')

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('## Post Save Signal ##')
    print(f'Instance: {instance}')
    print(f'Sender: {sender}')
    print(f'Kwargs: {kwargs}')

@receiver(pre_delete, sender=Car)   
def car_pre_delete(sender, instance, **kwargs):
    print('## Pre Delete Signal ##')
    print(f'Instance: {instance}')
    print(f'Sender: {sender}')
    print(f'Kwargs: {kwargs}')

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('## Post Delete Signal ##')
    print(f'Instance: {instance}')
    print(f'Sender: {sender}')
    print(f'Kwargs: {kwargs}')
