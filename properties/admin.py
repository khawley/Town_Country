from properties.models import Homes
from properties.models import Photos
from django.contrib import admin

class PhotosInline(admin.StackedInline):
    model = Photos
    extra = 3

class HomeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': (('type', 'house_type')),}),
        ('House Details', {'fields': (('str_addr', 'city'),('beds', 'baths', 'price'), ('description'),),}),
    ]
    inlines = [PhotosInline]
    
admin.site.register(Homes, HomeAdmin)