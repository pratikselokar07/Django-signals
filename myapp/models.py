from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    roll_no=models.SmallIntegerField()

    def __str__(self):
        return self.name


from django.db.models.signals import post_migrate,post_save,pre_delete
from django.dispatch import receiver

@receiver(post_migrate)
def migrations_done(sender, **kwargs):
    # do something when migrations are done
    print("Migrations done!")

# post_save method
@receiver(post_save, sender=Student) 
def create_product(sender, instance, **kwargs):
    print("Save method is called") 


@receiver(pre_delete, sender=Student)
def student_deleted(sender, instance, **kwargs):
    # do something when a Student instance is deleted
    print(f"The student {instance.name} ({instance.roll_no}) is deleted .")
