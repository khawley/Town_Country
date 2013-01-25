from properties.models import Home
from properties.models import Photo
from django.contrib import admin
from django.db import models
from snippets.models import AdminImageWidget

class PhotoInline(admin.TabularInline):
	model = Photo
	extra = 3
	formfield_overrides = {
        models.CharField: {'label': 'Image Label/description'},
        models.ImageField: {'widget': AdminImageWidget()},
    }
	"""fieldsets = [
		('Extra Photos' {'fields': ['name', 'img', 'img_thumb']})
	]"""

class HomeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			   {'fields': [('type', 'house_type')],}),
		('House Details', {'fields': [('str_addr', 'city'),('beds', 'baths', 'price'), ('description'),],}),
		('Main exterior photo', {'fields': ['main_photo', ],}),
	]
	inlines = [PhotoInline]
	
	list_display=('str_addr', 'type', 'house_type', 'date', 'contains_photo')
	
admin.site.register(Home, HomeAdmin)