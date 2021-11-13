from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class Navbar(models.Model):
    item = models.CharField(max_length=50)
    url = models.CharField(max_length=500, blank=True, null=True)
    child_items = models.ManyToManyField('NavbarItem', related_name='navitems', verbose_name='child_item')

    class Meta:
        verbose_name_plural = 'Навбар (эл)'
        verbose_name = 'Навбар (эл)'

    def __str__(self):
        return self.item


class NavbarItem(models.Model):
    child_item = models.CharField(max_length=50)
    url = models.CharField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Навбар (эл)'
        verbose_name = 'Навбар (эл)'

    def __str__(self):
        return self.child_item


class Footer(models.Model):
    logo = models.ImageField()
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    social_media = models.ImageField()
    social_media_link = models.CharField(max_length=255)
    sub_title = models.ManyToManyField('NavbarItem')

    class Meta:
        verbose_name_plural = 'Футер'

    def __str__(self):
        return self.title


class CarouselNews(models.Model):
    title = models.CharField(max_length=150)
    text = RichTextField()
    img = models.ImageField()

    class Meta:
        verbose_name_plural = 'Каруселлар'
        verbose_name = 'Карусель'

    def __str__(self):
        return self.title


class MineralResources(models.Model):
    title = models.CharField(max_length=100)
    button_txt = models.CharField(max_length=100)
    button_link = models.CharField(max_length=255)
    img = models.ImageField()

    class Meta:
        verbose_name_plural = "Минерал ресурслар"
        verbose_name = "Минерал ресурслар"

    def __str__(self):
        return self.title


class TwoMaps(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=200)
    button_txt = models.CharField(max_length=100)
    button_link = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Харита'
        verbose_name = 'Харита'


class CompanyPurpose(models.Model):
    title = models.CharField(max_length=150)
    text = RichTextField()

    class Meta:
        verbose_name_plural = 'Асосий мақсадлар'
        verbose_name = 'Асосий мақсадлар'

    def __str__(self):
        return self.title


class CompanyTasks(models.Model):
    title = models.CharField(max_length=150)
    company_tasks_items = models.ManyToManyField('CompanyTasksItems', related_name='tasksitems', verbose_name='child_item')

    class Meta:
        verbose_name_plural = 'Асосий вазифалар'
        verbose_name = 'Асосий вазифалар'

    def __str__(self):
        return self.title


class CompanyTasksItems(models.Model):
    text = RichTextField()

    class Meta:
        verbose_name_plural = 'Асосий вазифалар (Элем)'
        verbose_name = 'Асосий вазифалар (Элем)'

    def __str__(self):
        return f"{str(self.text)[0:20]}..."


class Auditory(models.Model):
    group_number = models.IntegerField()
    text = RichTextField()

    class Meta:
        verbose_name_plural = 'Мақсадли аудитория'
        verbose_name = 'Мақсадли аудитория'

    def __str__(self):
        return f"{str(self.text)[0:20]}..."


class Staff(models.Model):
    full_name = models.CharField(max_length=155)
    info = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Ходимлар'
        verbose_name = 'Ходим'

    def __str__(self):
        return self.full_name


class ProjectExpertise(models.Model):
    text = RichTextField()

    class Meta:
        verbose_name_plural = 'Лойиха хужжатларини экспертизаси'
        verbose_name = 'Лойиха хужжатларини экспертизаси'

    def __str__(self):
        return f"{str(self.text)[0:30]}..."


class YouthUnion(models.Model):
    text = RichTextField()

    class Meta:
        verbose_name_plural = 'Ёшлар иттифоқи'
        verbose_name = 'Ёшлар иттифоқи'


# page-8, i.e. vazirlar maxkamasining qarori, as well as p-9-10


class GeoInfo(models.Model):
    title = models.CharField(max_length=155)
    text = RichTextField()

    class Meta:
        verbose_name_plural = "Геологик малумотлар тўплами"
        verbose_name = "Геологик малумотлар тўплами"

    def __str__(self):
        return self.title


class ResourceBase(models.Model):
    region_name = models.CharField(max_length=200)
    excel_file = models.FileField()

    class Meta:
        verbose_name_plural = 'Минерал ресурслар базаси'
        verbose_name = 'Минерал ресурслар базаси'

    def __str__(self):
        return self.region_name


class Chapters(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150, blank=True)
    chapter_items = models.ForeignKey('ChaptersItems', on_delete=models.CASCADE, verbose_name="Bo'lim")

    class Meta:
        verbose_name_plural = "Бўлимлар"

    def __str__(self):
        return self.title


class ChaptersItems(models.Model):
    text = RichTextField()

    class Meta:
        verbose_name_plural = "Бўлимлар (Элем)"
        verbose_name = "Бўлимлар (Элем)"

    def __str__(self):
        return f"{str(self.text)[0:20]}..."


class Office(models.Model):
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Манзил ва телефон'
        verbose_name = 'Манзил ва телефон'

    def __str__(self):
        return self.address


class Laws(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    text = RichTextField()
    file = models.FileField()

    class Meta:
        verbose_name = 'Қарорлар'
        verbose_name_plural = 'Қарорлар'

    def __str__(self):
        return f"{str(self.title)[0:25]}"


class ProfConnections(models.Model):
    text = RichTextField()

    class Meta:
        verbose_name = 'Хисобот олиш учун масъулларнинг алоқалари'
        verbose_name_plural = 'Хисобот олиш учун масъулларнинг алоқалари'

    def __str__(self):
        return f"{str(self.text)[0:25]}"


class ReportAcceptance(models.Model):
    text = RichTextField()

    class Meta:
        verbose_name = 'Хисоботни қабул қилиш'
        verbose_name_plural = 'Хисоботларни кабул қилиш'

    def __str__(self):
        return f"{str(self.text)[0:25]}"


class University(models.Model):
    text = RichTextField()
    img = models.ImageField()

    class Meta:
        verbose_name = "Университет тадқиқотлари"
        verbose_name_plural = "Университет тадқиқотлари"

    def __str__(self):
        return f"{str(self.text)[0:30]}"


class News(models.Model):
    img = models.ImageField()
    text = models.CharField(max_length=500)
    date = models.DateField()

    class Meta:
        verbose_name = "Олиб борилаётган ишлар"
        verbose_name_plural = "Олиб борилаётган ишлар"

    def __str__(self):
        return f"{str(self.text)[0:30]}"


class ExcelForm(models.Model):
    resource = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    condition_a_b_c1 = models.CharField(max_length=155)
    condition_a_b_c2 = models.CharField(max_length=155)
    condition_c2 = models.IntegerField()
    exploitation = models.CharField(max_length=255)
    absorption_level = models.CharField(max_length=255)
    number_explot = models.CharField(max_length=155)
    license = models.DateField()
    prod_quantity = models.FloatField()
    affiliation = models.CharField(max_length=255)
    affirmation_year = models.CharField(max_length=155)
    protocol_num = models.IntegerField()
    raw_material = models.CharField(max_length=155)
    region = models.CharField(max_length=155)
    dist = models.CharField(max_length=155)

    class Meta:
        verbose_name_plural = "Excel формалар"
        verbose_name = "Excel форма"

    def __str__(self):
        return self.region


class BookkeepingReport(models.Model):
    text = models.CharField(max_length=255)
    excel_file = models.FileField()

    class Meta:
        verbose_name_plural = 'Буғалтерия хисоботлари'
        verbose_name = 'Буғалтерия хисоботи'

    def __str__(self):
        return self.excel_file

