# Generated by Django 2.2 on 2020-06-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0011_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
