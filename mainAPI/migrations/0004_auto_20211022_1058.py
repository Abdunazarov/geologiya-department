# Generated by Django 3.2.8 on 2021-10-22 10:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPI', '0003_auto_20211022_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('group_number', models.IntegerField()),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='companytasksitems',
            options={'verbose_name': 'Asosiy vazifalar (Elem)', 'verbose_name_plural': 'Asosiy vazifalar (Elem)'},
        ),
        migrations.AlterModelOptions(
            name='navbar',
            options={'verbose_name': 'Navbar (Elem)', 'verbose_name_plural': 'Navbar (Elem)'},
        ),
    ]
