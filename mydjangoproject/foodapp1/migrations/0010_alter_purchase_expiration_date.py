# Generated by Django 4.1.4 on 2022-12-22 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp1', '0009_alter_purchase_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
