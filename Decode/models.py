from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DecodedData(models.Model):
    Starting_Index = models.IntegerField(blank=True, null=True)
    Ghap = models.IntegerField(blank=True, null=True)
    Add_a_Value = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)