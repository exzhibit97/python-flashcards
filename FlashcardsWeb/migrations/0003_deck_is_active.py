# Generated by Django 3.0 on 2019-12-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlashcardsWeb', '0002_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
