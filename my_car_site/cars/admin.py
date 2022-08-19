from django.contrib import admin
from cars.models import Car  # dunno why cars.models marked as mistake. maby because project is pure python?


# Register your models here.

# admin.site.register(Car)


class CarAdmin(admin.ModelAdmin):
    # customizing admin panel for Car model
    # fields = ['year', 'brand']  # if you want to change order of field in admin panel
    fieldsets = [
        ('TIME INFORMATION', {'fields': ['year']}),  # will add labels with titles for your field or multiple fields
        ('CAR INFORMATION', {'fields': ['brand']}),
    ]
    # additional information look in documentation of django


admin.site.register(Car, CarAdmin)
