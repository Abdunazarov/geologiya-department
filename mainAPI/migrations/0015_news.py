# Generated by Django 3.2.8 on 2021-11-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPI', '0014_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('text', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Olib borilayotgan ishlar',
                'verbose_name_plural': 'Olib borilayotgan ishlar',
            },
        ),
    ]