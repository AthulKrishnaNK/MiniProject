from django.db import models

# Create your models here.

class Vendor(models.Model):
    v_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'vendor'

