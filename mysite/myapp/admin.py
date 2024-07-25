from django.contrib import admin

from .models import Chairs, Main_GameChairs, Main_OfficeChairs, Main_DirChairs, Main_OrtChairs

admin.site.register(Main_GameChairs)
admin.site.register(Main_OfficeChairs)
admin.site.register(Main_DirChairs)
admin.site.register(Main_OrtChairs)
admin.site.register(Chairs)