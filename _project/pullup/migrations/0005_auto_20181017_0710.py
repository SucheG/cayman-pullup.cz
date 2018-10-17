# Generated by Django 2.1 on 2018-10-17 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pullup', '0004_auto_20181013_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvik',
            name='popis',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='cvik',
            name='telo',
            field=models.ManyToManyField(blank=True, to='pullup.Telo'),
        ),
        migrations.AlterField(
            model_name='cvik',
            name='varianty',
            field=models.ManyToManyField(blank=True, through='pullup.Varianta', to='pullup.Cvik'),
        ),
        migrations.AlterField(
            model_name='cvik',
            name='vybaveni',
            field=models.ManyToManyField(blank=True, through='pullup.Potrebuje', to='pullup.Vybaveni'),
        ),
        migrations.AlterField(
            model_name='media',
            name='popis',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='misto',
            name='popis',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='misto',
            name='vybaveni',
            field=models.ManyToManyField(blank=True, to='pullup.Vybaveni'),
        ),
        migrations.AlterField(
            model_name='telo',
            name='popis',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='vybaveni',
            name='popis',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
