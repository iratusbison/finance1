# Generated by Django 4.0.6 on 2023-10-28 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmanager', '0032_insection_investment_inpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
