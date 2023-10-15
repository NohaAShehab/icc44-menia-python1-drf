from django.db import models

# Create your models here.


class Student(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(unique=True, null=True, blank=True)
    grade = models.IntegerField(default=0)
    image = models.ImageField(upload_to='students/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_students(cls):
        return cls.objects.all()