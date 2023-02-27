from django.db import models

# Create your models here.

class State(models.Model):
    name=models.CharField(max_length=50)
    capital=models.CharField(max_length=50)
    area=models.BigIntegerField(null=True)
    image=models.ImageField()
    population=models.JSONField(encoder=None)
    ruling_party=models.CharField(max_length=50)
    cheif_minister=models.CharField(max_length=50)
    home_minister=models.CharField(max_length=50)
    region=models.CharField(max_length=50)
    litreacy=models.DecimalField(max_digits=4,decimal_places=2,null=True)
    gdp=models.JSONField(encoder=None,null=True)
    coastal=models.BooleanField()

    def __str__(self):
        return self.name

