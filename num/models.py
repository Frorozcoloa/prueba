from django.db import models

from jsonfield import JSONField



# Create your models here.

class Num(models.Model):
    the_json = JSONField()
