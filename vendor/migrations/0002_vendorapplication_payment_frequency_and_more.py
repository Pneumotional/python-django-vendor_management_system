# Generated by Django 5.0.3 on 2025-01-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorapplication',
            name='payment_frequency',
            field=models.CharField(choices=[('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly')], default='MONTHLY', max_length=10),
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='payment_frequency',
            field=models.CharField(choices=[('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly')], default='MONTHLY', max_length=10),
        ),
    ]
