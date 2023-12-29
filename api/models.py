import uuid
from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100,default='')
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=36, default=uuid.uuid4, unique=True, editable=False)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)

class Purchase_order(models.Model):
    po_number = models.CharField(max_length=36, default=uuid.uuid4, unique=True, editable=False)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField(null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100,default='',choices=[('pending','pending'),('completed','completed'),('canceled','canceled')])
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

class Hist_performance(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    hist_date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    