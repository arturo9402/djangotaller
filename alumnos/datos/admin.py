from django.contrib import admin

# Register your models here.
from .models import InfoGeneral

class InfoGeneralAdmin(admin.ModelAdmin):
    pass

admin.site.register(InfoGeneral,InfoGeneralAdmin)

