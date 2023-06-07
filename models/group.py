from django.db import models

class Group(models.Model):
    id          = models.BigAutoField(primary_key=True)
    name        = models.CharField(max_length=30, null=False)