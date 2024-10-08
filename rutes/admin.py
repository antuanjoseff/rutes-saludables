from django.contrib import admin
from .models import Campus, Trail, TrailType, Point, InterestPoint
from tabbed_admin import TabbedModelAdmin
from .forms import PointAdminForm, TrailAdminForm

# from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin, SummernoteWidget


# change admin title
# admin.site.site_header = 'Gestor de continguts dels itineraris saludables de la UB'
# admin.site.index_template = 'admin/rutes/index.html' # overwritte admin index template



class PointInline(admin.StackedInline):
    model = Point
    extra = 1
    form = PointAdminForm



class TrailAdmin(TabbedModelAdmin):
    """Trail Admin"""

    model = Trail
    form = TrailAdminForm

    tab_campus = (
        ('Visibilitat', {
            'fields': ('published',)
        }),
        ('Descripció', {
            'fields': ('title',)
        }),
    )

    tab_geom = (
        ('Localització', {
            'fields': ('campus','geom',)
        }),
    )

    tab_categories = (
        ('Categories', {
            'fields': ('type','distance','duration',)
        }),
    )

    tab_resources = (
        PointInline,
    )
    
    tabs = [
        ('Campus', tab_campus),
        ('Geom', tab_geom),
        ('Categories', tab_categories),
        ('Recursos', tab_resources)
    ]



admin.site.register(Campus)
admin.site.register(TrailType)
admin.site.register(Trail, TrailAdmin)
admin.site.register(InterestPoint)

