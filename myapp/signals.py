from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
    
# post_save method
@receiver(post_save, sender=Student) 
def create_product(sender, instance, **kwargs):
    print("Save method is called") 