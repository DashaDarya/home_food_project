# Generated by Django 4.1.4 on 2022-12-25 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp1', '0010_alter_purchase_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
