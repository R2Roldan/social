# Generated by Django 3.2.2 on 2021-11-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20211108_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialpost',
            name='shared_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
