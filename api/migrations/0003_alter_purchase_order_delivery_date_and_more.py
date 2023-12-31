# Generated by Django 4.1.13 on 2023-12-12 12:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_vendor_average_response_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase_order",
            name="delivery_date",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="purchase_order",
            name="order_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="purchase_order",
            name="po_number",
            field=models.CharField(
                default=uuid.uuid4, editable=False, max_length=36, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="purchase_order",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "pending"),
                    ("completed", "completed"),
                    ("canceled", "canceled"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]
