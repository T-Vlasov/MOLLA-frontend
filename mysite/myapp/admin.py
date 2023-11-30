from django.contrib import admin

from .models import OfficeChairs, GameChairs, OrtChairs

admin.site.register(OfficeChairs)
admin.site.register(GameChairs)
admin.site.register(OrtChairs)