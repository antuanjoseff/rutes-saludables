from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator


# Create your models here.
class User(AbstractUser):
    pass
    

class TrailType(models.Model):
    """Model tipus itinerari"""

    title = models.CharField(max_length=40, verbose_name='Títol')

    def __str__(self):
        """Repr."""
        return self.title


    class Meta(object):
        """Meta"""

        verbose_name = 'Tipologia itinerari'
        verbose_name_plural = "Tipologia d'itineraris"


class Campus(models.Model):
    """Model Campus"""

    title = models.CharField(max_length=250, verbose_name='Títol')

    def __str__(self):
        """Repr."""
        return self.title


    class Meta(object):
        """Meta"""

        verbose_name = 'Campus'
        verbose_name_plural = 'Campus'


class Point(models.Model):
    """Model  de punts"""

    title = models.CharField(max_length=250, verbose_name='Títol', null=True, blank=True)
    description = models.TextField(verbose_name='Descripció', null=True, blank=True)
    trail = models.ForeignKey('Trail', on_delete=models.CASCADE, related_name='points', null=True, blank=True, verbose_name='Trail')
    geom = models.PointField(null=True, blank=True, verbose_name='Geometria')
    order = models.IntegerField(null=True, blank=True, verbose_name='Ordre')

    def __str__(self):
        """Repr."""
        return self.title

    class Meta(object):
        """Meta"""

        unique_together = ('trail', 'order', )
        verbose_name = 'Punt'
        verbose_name_plural = 'Punts'


class InterestPoint(models.Model):
    """Model de punts d'interès"""

    title = models.CharField(max_length=250, verbose_name='Títol', null=True, blank=True)
    description = models.TextField(verbose_name='Descripció', null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    geom = models.PointField(null=True, blank=True, verbose_name='Geometria')

    def __str__(self):
        """Repr."""
        return self.title

    class Meta(object):
        """Meta"""

        verbose_name = 'Punt interès'
        verbose_name_plural = "Punts d'interès"



    def get_absolute_url(self):
        return reverse("posts:quill-post-detail", args=[self.pk])


class Trail(models.Model):
    """Model Itineraris"""

    title = models.CharField(max_length=250, verbose_name='Títol', null=True, blank=True)
    campus = models.ForeignKey('Campus', on_delete=models.SET_NULL, null=True,  blank=True, related_name='trails', verbose_name='Campus')
    geom = models.MultiLineStringField(null=True, blank=True)
    published = models.BooleanField(default=True, verbose_name='Publicat', blank=True)
    type = models.ForeignKey('TrailType', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Tipologia')
    distance = models.FloatField(validators=[MinValueValidator(0.0)], help_text='Distància en km', verbose_name='Distància', null=True, blank=True)
    duration = models.PositiveIntegerField(help_text='Durada en minuts', verbose_name='Durada', null=True, blank=True)


    def __str__(self):
        """Repr."""
        return self.title

    class Meta(object):
        """Meta"""

        verbose_name = 'Itinerari'
        verbose_name_plural = 'Itineraris'

