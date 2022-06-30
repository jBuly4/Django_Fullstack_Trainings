from django.db import models

# Create your models here.
class Car(models.Model):
    # pk will be created automatically
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self) -> str:
        return f"Car is {self.brand} of {self.year}"