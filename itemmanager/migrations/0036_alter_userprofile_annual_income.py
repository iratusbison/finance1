# Generated by Django 4.0.6 on 2023-10-30 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmanager', '0035_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='annual_income',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
    ]
