from django.contrib import admin
# from .models import related models
from .models import CarMake,CarModel




# Register your models here.

# CarModelInline class
class CarModelInline(admin.ModelAdmin):
    model=CarModel
    extra=0

class CarModelAdmin(admin.ModelAdmin):
    pass

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin:
    inlines=[CarModelInline]

# Register models here
admin.site.register(CarMake,CarModel)