from django.db import models

class MomCat(models.Model):
    name = models.CharField(max_length=255, null=False)
    age = models.IntegerField()
    owners_name = models.CharField(max_length=255, null=False)

class Kitten(models.Model):
    name = models.CharField(max_length=255, null=False)
    age_in_months = models.IntegerField()
    momcat = models.ForeignKey('MomCat', related_name='kittens', on_delete=models.CASCADE)
