# Generated by Django 2.1.7 on 2021-04-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0005_rule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='encours',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='taux',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='volume',
            field=models.CharField(max_length=30),
        ),
    ]