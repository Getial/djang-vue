from django.contrib import admin
from .models import Destination, VacationPlan, Blog

# Register your models here.
admin.site.register(Destination)
admin.site.register(VacationPlan)
admin.site.register(Blog)