# Generated by Django 5.0 on 2024-01-04 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
            ],
        ),
    ]