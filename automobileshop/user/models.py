from django.db import models

# Create your models here.


class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=40)
    address = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'user'


