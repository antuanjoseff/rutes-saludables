from django import forms
from .models import Point, Trail
import django.contrib.gis.forms as gis_forms
from django.contrib.gis.forms.widgets import OSMWidget

class PointAdminForm(forms.ModelForm):
    model = Point

    geom = gis_forms.PointField(
        srid=4326,
        widget=gis_forms.OSMWidget(
            attrs={
                "map_width": 800,
                "map_srid": 4326,
                "map_height": 50,
                "default_lat": 41.246292,
                "default_lon": 3.116226,
                "default_zoom": 7,
            }
        ),
    )

class TrailAdminForm(forms.ModelForm):
    model = Trail

    geom = gis_forms.MultiLineStringField(
        srid=4326,
        widget=gis_forms.OSMWidget(
            attrs={
                "map_width": 1000,
                "map_srid": 4326,
                "map_height": 500,
                "default_lat": 41.9763,
                "default_lon":  2.816610,
                "default_zoom": 14,
            }
        ),
    )


