# Generated by Django 4.1.3 on 2022-12-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
