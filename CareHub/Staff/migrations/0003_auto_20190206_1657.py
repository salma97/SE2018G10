# Generated by Django 2.1.2 on 2019-02-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0002_auto_20190206_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
