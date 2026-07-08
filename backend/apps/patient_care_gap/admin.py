from django.contrib import admin
from .models import Patient, CareGap

# Register your models here.
admin.site.register(Patient)
admin.site.register(CareGap)
