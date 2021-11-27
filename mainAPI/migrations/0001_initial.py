# Generated by Django 3.2.8 on 2021-11-27 08:44

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationLoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_phone', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name': 'Ариза берадиган жой тўғрисида маълумот',
                'verbose_name_plural': 'Ариза берадиган жой тўғрисида маълумот',
            },
        ),
        migrations.CreateModel(
            name='Auditory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.IntegerField()),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Мақсадли аудитория',
                'verbose_name_plural': 'Мақсадли аудитория',
            },
        ),
        migrations.CreateModel(
            name='BankInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MFO_number', models.IntegerField()),
                ('account_number', models.IntegerField()),
                ('bank_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Хизмат кўрсатувчи банк бўйича маълумотлар',
                'verbose_name_plural': 'Хизмат кўрсатувчи банк бўйича маълумотлар',
            },
        ),
        migrations.CreateModel(
            name='BookkeepingReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('excel_file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Буғалтерия хисоботи',
                'verbose_name_plural': 'Буғалтерия хисоботлари',
            },
        ),
        migrations.CreateModel(
            name='Businessman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stir', models.IntegerField()),
                ('company_name', models.CharField(max_length=255)),
                ('ifut', models.IntegerField()),
                ('ceo_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Тадбиркор',
                'verbose_name_plural': 'Тадбиркор',
            },
        ),
        migrations.CreateModel(
            name='CarouselNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', ckeditor.fields.RichTextField()),
                ('img', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Карусель',
                'verbose_name_plural': 'Каруселлар',
            },
        ),
        migrations.CreateModel(
            name='ChaptersItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Бўлимлар (Элем)',
                'verbose_name_plural': 'Бўлимлар (Элем)',
            },
        ),
        migrations.CreateModel(
            name='CompanyPurpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Асосий мақсадлар',
                'verbose_name_plural': 'Асосий мақсадлар',
            },
        ),
        migrations.CreateModel(
            name='CompanyTasksItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Асосий вазифалар (Элем)',
                'verbose_name_plural': 'Асосий вазифалар (Элем)',
            },
        ),
        migrations.CreateModel(
            name='GeoInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Геологик малумотлар тўплами',
                'verbose_name_plural': 'Геологик малумотлар тўплами',
            },
        ),
        migrations.CreateModel(
            name='Laws',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('text', ckeditor.fields.RichTextField()),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Қарорлар',
                'verbose_name_plural': 'Қарорлар',
            },
        ),
        migrations.CreateModel(
            name='MineInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Кон ҳақида',
                'verbose_name_plural': 'Кон ҳақида',
            },
        ),
        migrations.CreateModel(
            name='MineralResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('button_txt', models.CharField(max_length=100)),
                ('button_link', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Минерал ресурслар',
                'verbose_name_plural': 'Минерал ресурслар',
            },
        ),
        migrations.CreateModel(
            name='NavbarItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_item', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Навбар (эл)',
                'verbose_name_plural': 'Навбар (эл)',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('text', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Олиб борилаётган ишлар',
                'verbose_name_plural': 'Олиб борилаётган ишлар',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Манзил ва телефон',
                'verbose_name_plural': 'Манзил ва телефон',
            },
        ),
        migrations.CreateModel(
            name='ProfConnections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Хисобот олиш учун масъулларнинг алоқалари',
                'verbose_name_plural': 'Хисобот олиш учун масъулларнинг алоқалари',
            },
        ),
        migrations.CreateModel(
            name='ProjectExpertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Лойиха хужжатларини экспертизаси',
                'verbose_name_plural': 'Лойиха хужжатларини экспертизаси',
            },
        ),
        migrations.CreateModel(
            name='ReportAcceptance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Хисоботни қабул қилиш',
                'verbose_name_plural': 'Хисоботларни кабул қилиш',
            },
        ),
        migrations.CreateModel(
            name='ResourceBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=200)),
                ('excel_file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Минерал ресурслар базаси',
                'verbose_name_plural': 'Минерал ресурслар базаси',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('full_name', models.CharField(max_length=155)),
                ('info', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Ходим',
                'verbose_name_plural': 'Ходимлар',
            },
        ),
        migrations.CreateModel(
            name='TwoMaps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(max_length=200)),
                ('button_txt', models.CharField(max_length=100)),
                ('button_link', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Харита',
                'verbose_name_plural': 'Харита',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
                ('img', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Университет тадқиқотлари',
                'verbose_name_plural': 'Университет тадқиқотлари',
            },
        ),
        migrations.CreateModel(
            name='YouthUnion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Ёшлар иттифоқи',
                'verbose_name_plural': 'Ёшлар иттифоқи',
            },
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=500, null=True)),
                ('child_items', models.ManyToManyField(related_name='navitems', to='mainAPI.NavbarItem', verbose_name='child_item')),
            ],
            options={
                'verbose_name': 'Навбар (эл)',
                'verbose_name_plural': 'Навбар (эл)',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('social_media', models.ImageField(upload_to='')),
                ('social_media_link', models.CharField(max_length=255)),
                ('sub_title', models.ManyToManyField(to='mainAPI.NavbarItem')),
            ],
            options={
                'verbose_name_plural': 'Футер',
            },
        ),
        migrations.CreateModel(
            name='CompanyTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('company_tasks_items', models.ManyToManyField(related_name='tasksitems', to='mainAPI.CompanyTasksItems', verbose_name='child_item')),
            ],
            options={
                'verbose_name': 'Асосий вазифалар',
                'verbose_name_plural': 'Асосий вазифалар',
            },
        ),
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(blank=True, max_length=150)),
                ('chapter_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainAPI.chaptersitems', verbose_name="Bo'lim")),
            ],
            options={
                'verbose_name_plural': 'Бўлимлар',
            },
        ),
    ]
