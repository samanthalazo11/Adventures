from django.contrib import admin
from .models import Destination, Restauraunts, Excursions

# Register your models here.
admin.site.register(Destination)
admin.site.register(Restauraunts)
admin.site.register(Excursions)
