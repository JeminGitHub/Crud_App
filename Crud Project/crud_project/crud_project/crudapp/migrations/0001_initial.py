# Generated by Django 4.2 on 2023-06-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField()),
                ('item_name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]