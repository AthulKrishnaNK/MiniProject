from django.db import models
from product.models import Product
# Create your models here.

class Orders(models.Model):
    o_id = models.AutoField(primary_key=True)
    # p_id = models.IntegerField()
    p=models.ForeignKey(Product,to_field='p_id',on_delete=models.CASCADE)
    v_id = models.IntegerField()
    status = models.CharField(max_length=20)
    total = models.CharField(max_length=20)
    quantity = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'orders'

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    cart_id = models.IntegerField()
    card_no = models.IntegerField()
    cvv = models.IntegerField()
    exp_date = models.DateField()
    holder_name = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    total = models.CharField(max_length=30)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'payment'

