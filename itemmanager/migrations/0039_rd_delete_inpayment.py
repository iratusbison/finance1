# Generated by Django 4.0.6 on 2023-11-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmanager', '0038_remove_investment_investment_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('period_months', models.IntegerField()),
                ('installment_cycle', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='InPayment',
        ),
    ]
