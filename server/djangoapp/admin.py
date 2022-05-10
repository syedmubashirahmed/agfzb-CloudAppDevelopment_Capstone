from django.contrib import admin
# from .models import related models
from .models import CarMake,CarModel

class CarModelInline(admin.StackedInline):
    model=CarModel
    extra=2

class CarMakeAdmin(admin.ModelAdmin):
    fileds=["carname","description"]
    inlines=[CarModelInline]

# Register models here
admin.site.register(CarMake,CarMakeAdmin)
