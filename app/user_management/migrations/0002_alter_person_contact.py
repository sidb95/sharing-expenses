# Generated by Django 5.0.6 on 2024-10-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
