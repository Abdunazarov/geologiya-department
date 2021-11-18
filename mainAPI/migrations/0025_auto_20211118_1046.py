# Generated by Django 3.2.8 on 2021-11-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPI', '0024_auto_20211118_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationloc',
            name='dist',
            field=models.CharField(choices=[(1, '79979')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='applicationloc',
            name='raw_material',
            field=models.CharField(choices=[(1, '98797')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='applicationloc',
            name='region',
            field=models.CharField(choices=[(1, '9879')], max_length=250, null=True),
        ),
    ]