from django.contrib import admin
# from .models import related models
from .models import CarMake,CarModel

admin.site.register(CarMake,CarModel)


# Register your models here.

# CarModelInline class
class CarModelInline(admin.ModelAdmin):
    pass

class CarModelAdmin(admin.ModelAdmin):
    pass

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin:
    inlines=[CarModelInline]

# Register models here
