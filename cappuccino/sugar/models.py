from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return f"Country: {self.name}"

    class Meta:
        verbose_name_plural = 'Countries'


class Food(models.Model):
    name = models.TextField()
    origin = models.OneToOneField(Country, on_delete=models.SET_NULL,
                                  null=True)

    def __str__(self):
        return f"{self.name} - {self.origin.name}"

    class Meta:
        ordering = ['name']
