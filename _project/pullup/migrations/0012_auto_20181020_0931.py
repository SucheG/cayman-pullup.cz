# Generated by Django 2.1 on 2018-10-20 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pullup', '0011_auto_20181018_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
                ('kod', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='media',
            old_name='nazev',
            new_name='unique',
        ),
        migrations.AddField(
            model_name='potrebuje',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='varianta',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='potrebuje',
            unique_together={('cvik', 'vybaveni')},
        ),
        migrations.AddField(
            model_name='media',
            name='typ',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='pullup.TypMedia'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='media',
            name='created_dt',
        ),
        migrations.RemoveField(
            model_name='media',
            name='popis',
        ),
        migrations.RemoveField(
            model_name='media',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='media',
            name='updated_dt',
        ),
        migrations.AlterUniqueTogether(
            name='media',
            unique_together={('unique', 'typ')},
        ),
    ]