# Generated by Django 2.0.2 on 2018-02-18 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180218_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verb',
            name='proposition',
            field=models.CharField(default='', max_length=100),
        ),
    ]