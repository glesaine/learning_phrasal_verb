# Generated by Django 2.0.2 on 2018-02-20 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180220_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verb',
            name='example',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='verb',
            name='meaning',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='verb',
            name='phrasal_verb',
            field=models.CharField(default='', max_length=100),
        ),
    ]
