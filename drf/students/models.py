from django.db import models

# Create your models here.


class Student(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(unique=True, null=True, blank=True)
    grade = models.IntegerField(default=0)
    image = models.ImageField(upload_to='students/images/', null=True, blank=True)


    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_students(cls):
        return cls.objects.all()