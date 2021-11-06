# Generated by Django 3.2.8 on 2021-11-03 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPI', '0018_auto_20211103_1030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auditory',
            options={'verbose_name': 'Мақсадли аудитория', 'verbose_name_plural': 'Мақсадли аудитория'},
        ),
        migrations.AlterModelOptions(
            name='carouselnews',
            options={'verbose_name': 'Карусел', 'verbose_name_plural': 'Каруселлар'},
        ),
        migrations.AlterModelOptions(
            name='chapters',
            options={'verbose_name_plural': 'Бўлимлар'},
        ),
        migrations.AlterModelOptions(
            name='chaptersitems',
            options={'verbose_name': 'Бўлимлар (Элем)', 'verbose_name_plural': 'Бўлимлар (Элем)'},
        ),
        migrations.AlterModelOptions(
            name='companypurpose',
            options={'verbose_name': 'Асосий мақсадлар', 'verbose_name_plural': 'Асосий мақсадлар'},
        ),
        migrations.AlterModelOptions(
            name='companytasks',
            options={'verbose_name': 'Асосий вазифалар', 'verbose_name_plural': 'Асосий вазифалар'},
        ),
        migrations.AlterModelOptions(
            name='companytasksitems',
            options={'verbose_name': 'Асосий вазифалар (Элем)', 'verbose_name_plural': 'Асосий вазифалар (Элем)'},
        ),
        migrations.AlterModelOptions(
            name='excelform',
            options={'verbose_name': 'Excel форма', 'verbose_name_plural': 'Excel формалар'},
        ),
        migrations.AlterModelOptions(
            name='geoinfo',
            options={'verbose_name': 'Геологик малумотлар тўплами', 'verbose_name_plural': 'Геологик малумотлар тўплами'},
        ),
        migrations.AlterModelOptions(
            name='mineralresources',
            options={'verbose_name': 'Минерал ресурслар', 'verbose_name_plural': 'Минерал ресурслар'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Олиб борилаётган ишлар', 'verbose_name_plural': 'Олиб борилаётган ишлар'},
        ),
        migrations.AlterModelOptions(
            name='office',
            options={'verbose_name': 'Манзил ва телефон', 'verbose_name_plural': 'Манзил ва телефон'},
        ),
        migrations.AlterModelOptions(
            name='profconnections',
            options={'verbose_name': 'Хисобот олиш учун масъулларнинг алоқалари', 'verbose_name_plural': 'Хисобот олиш учун масъулларнинг алоқалари'},
        ),
        migrations.AlterModelOptions(
            name='projectexpertise',
            options={'verbose_name': 'Лойиха хужжатларини экспертизаси', 'verbose_name_plural': 'Лойиха хужжатларини экспертизаси'},
        ),
        migrations.AlterModelOptions(
            name='reportacceptance',
            options={'verbose_name': 'Хисоботни қабул қилиш', 'verbose_name_plural': 'Хисоботларни кабул қилиш'},
        ),
        migrations.AlterModelOptions(
            name='resourcebase',
            options={'verbose_name': 'Минерал ресурслар базаси', 'verbose_name_plural': 'Минерал ресурслар базаси'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Ходим', 'verbose_name_plural': 'Ходимлар'},
        ),
        migrations.AlterModelOptions(
            name='twomaps',
            options={'verbose_name': 'Харита', 'verbose_name_plural': 'Харита'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name': 'Университет тадқиқотлари', 'verbose_name_plural': 'Университет тадқиқотлари'},
        ),
        migrations.AlterModelOptions(
            name='youthunion',
            options={'verbose_name': 'Ёшлар иттифоқи', 'verbose_name_plural': 'Ёшлар иттифоқи'},
        ),
    ]