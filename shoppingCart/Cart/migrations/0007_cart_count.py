# Generated by Django 2.2 on 2020-06-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0006_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
