from django.db import models

# Create your models here.

class Complaint(models.Model):
    com_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=30)
    reply = models.CharField(max_length=30)
    v_id = models.IntegerField()
    u_id = models.IntegerField()
    date = models.DateField()
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'complaint'

