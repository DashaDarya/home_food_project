# Generated by Django 4.1.4 on 2022-12-27 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp1', '0013_alter_purchase_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodapp1.location'),
        ),
    ]
