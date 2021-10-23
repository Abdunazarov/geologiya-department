from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class Navbar(models.Model):
    item = models.CharField(max_length=50)
    url = models.CharField(max_length=500, blank=True, null=True)
    child_items = models.ManyToManyField('NavbarItem', related_name='navitems', verbose_name='child_item')

    class Meta:
        verbose_name_plural = 'Navbar (Elem)'
        verbose_name = 'Navbar (Elem)'

    def __str__(self):
        return self.item


class NavbarItem(models.Model):
    child_item = models.CharField(max_length=50)
    url = models.CharField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=False)

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
        verbose_name_plural = 'Footer'

    def __str__(self):
        return self.title


class CarouselNews(models.Model):
    title = models.CharField(max_length=150)
    text = RichTextField()
    img = models.ImageField()

    class Meta:
        verbose_name_plural = 'Karusellar'
        verbose_name = 'Karusel'

    def __str__(self):
        return self.title


class MineralResources(models.Model):
    title = models.CharField(max_length=100)
    button_txt = models.CharField(max_length=100)
    button_link = models.CharField(max_length=255)
    img = models.ImageField()

    def __str__(self):
        return self.title


class TwoMaps(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=200)
    button_txt = models.CharField(max_length=100)
    button_link = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Xarita'
        verbose_name = 'Xarita'


class CompanyPurpose(models.Model):
    title = models.CharField(max_length=150)
    text = RichTextField()

    class Meta:
        verbose_name_plural = 'Asosiy maqsadlar'
        verbose_name = 'Asosiy maqsad'

    def __str__(self):
        return self.title


class CompanyTasks(models.Model):
    title = models.CharField(max_length=150)
    company_tasks_items = models.ManyToManyField('CompanyTasksItems', related_name='tasksitems', verbose_name='child_item')

    class Meta:
        verbose_name_plural = 'Asosiy vazifalar'
        verbose_name = 'Asosiy vazifa'

    def __str__(self):
        return self.title


class CompanyTasksItems(models.Model):
    text = RichTextField()

    class Meta:
        verbose_name_plural = 'Asosiy vazifalar (Elem)'
        verbose_name = 'Asosiy vazifalar (Elem)'

    def __str__(self):
        return f"{str(self.text)[0:20]}..."


class Auditory(models.Model):
    group_number = models.IntegerField()
    text = RichTextField()

    class Meta:
        verbose_name_plural = 'Maqsadli auditoriya'
        verbose_name = 'Maqsadli auditoriya'

    def __str__(self):
        return f"{str(self.text)[0:20]}..."


class Staff(models.Model):
    full_name = models.CharField(max_length=155)
    info = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Xodimalar'
        verbose_name = 'Xodim'

    def __str__(self):
        return self.full_name


class ProjectExpertise(models.Model):
    text = RichTextField()

    class Meta:
        verbose_name_plural = 'Loyiha hujjatlarini ekspertizasi'
        verbose_name = 'Loyiha hujjatlarini ekspertizalari'

    def __str__(self):
        return f"{str(self.text)[0:30]}..."


class YouthUnion(models.Model):
    text = RichTextField()

    class Meta:
        verbose_name_plural = 'Yoshlar ittifoqi'
        verbose_name = 'Yoshlar ittifoqi'