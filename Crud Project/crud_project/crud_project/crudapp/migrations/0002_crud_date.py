# Generated by Django 4.2 on 2023-06-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crud',
            name='date',
            field=models.DateField(default='1997-12-12'),
            preserve_default=False,
        ),
    ]
