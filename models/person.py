from django.db import models

# Create your models here.
class Person(models.Model):
    id          = models.BigAutoField(primary_key=True)
    first_name  = models.CharField(max_length=30)
    last_name   = models.CharField(max_length=30)
    group       = models.ForeignKey(
        "Group",
        on_delete=models.CASCADE,
        null=True
    )