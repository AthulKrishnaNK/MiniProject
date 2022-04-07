from django.db import models

# Create your models here.
class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    wholesale_price = models.IntegerField()
    quantity = models.CharField(max_length=20)
    img = models.CharField(max_length=300)
    retail_price = models.IntegerField()
    description = models.CharField(max_length=50)
    v_id = models.IntegerField()
    spare_name = models.CharField(db_column='spare name', max_length=30)  # Field renamed to remove unsuitable characters.
    companyname = models.CharField(max_length=30)
    vehiclename = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'product'

