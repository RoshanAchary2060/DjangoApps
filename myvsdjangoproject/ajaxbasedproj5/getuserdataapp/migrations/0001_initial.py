# Generated by Django 5.0 on 2024-04-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('sal', models.IntegerField()),
                ('job', models.CharField(max_length=30)),
            ],
        ),
    ]
