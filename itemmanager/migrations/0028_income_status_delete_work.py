# Generated by Django 4.0.6 on 2023-10-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmanager', '0027_work_remove_investment_section_remove_loan_section_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]
