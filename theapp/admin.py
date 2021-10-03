from django.contrib import admin
from django.db import models
from .models import partner
# Register your models here.
@admin.register(partner)
class partnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'partner_id', 'cast', 'religion']