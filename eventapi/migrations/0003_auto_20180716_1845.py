# Generated by Django 2.0.7 on 2018-07-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapi', '0002_auto_20180716_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='kauaisuggestion',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(),
        ),
    ]
