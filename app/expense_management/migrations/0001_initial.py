# Generated by Django 5.0.6 on 2024-10-22 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.IntegerField(auto_created=True, unique=True)),
                ('amount', models.IntegerField()),
                ('users_expense', models.JSONField()),
            ],
        ),
    ]
