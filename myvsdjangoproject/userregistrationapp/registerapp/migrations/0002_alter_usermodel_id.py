# Generated by Django 5.0 on 2024-01-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
