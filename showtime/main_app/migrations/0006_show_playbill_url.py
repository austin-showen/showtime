# Generated by Django 4.2.2 on 2023-06-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_show_user_remove_show_seen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='playbill_url',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
