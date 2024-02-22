from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Country(models.Model):
    name = CountryField()

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
