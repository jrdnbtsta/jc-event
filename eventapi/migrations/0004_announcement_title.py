# Generated by Django 2.0.7 on 2018-07-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapi', '0003_auto_20180716_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
