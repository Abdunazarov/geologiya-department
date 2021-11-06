# Generated by Django 3.2.8 on 2021-10-22 10:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPurpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Asosiy maqsad',
                'verbose_name_plural': 'Asosiy maqsadlar',
            },
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name_plural': 'Footer'},
        ),
    ]