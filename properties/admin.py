from properties.models import Home
from properties.models import Photo
from django.contrib import admin

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 3

class HomeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': (('type', 'house_type')),}),
        ('House Details', {'fields': (('str_addr', 'city'),('beds', 'baths', 'price'), ('description'),),}),
    ]
    inlines = [PhotoInline]
    
admin.site.register(Home, HomeAdmin)