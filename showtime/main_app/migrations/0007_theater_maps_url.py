# Generated by Django 4.2.2 on 2023-06-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_show_playbill_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='theater',
            name='maps_url',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
