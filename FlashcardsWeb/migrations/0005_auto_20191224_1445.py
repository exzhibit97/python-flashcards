# Generated by Django 3.0 on 2019-12-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlashcardsWeb', '0004_auto_20191224_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='back',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='card',
            name='usageExample',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
