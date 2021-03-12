from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email

    class Meta :
        db_table = "employee"