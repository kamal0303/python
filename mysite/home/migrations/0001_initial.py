# Generated by Django 4.1.3 on 2022-11-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('surname', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
