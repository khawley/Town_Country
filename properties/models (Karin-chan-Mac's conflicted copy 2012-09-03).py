from django.db import models
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
#from django.utils import timezone

# Create your models here.

class Home (models.Model):
	str_addr = models.CharField(max_length=50)
	city_choices=(('Oakdale', 'Oakdale'), ('Riverbank', 'Riverbank'), ('Modesto', 'Modesto'), ('Escalon', 'Escalon'),)
	city = models.CharField(max_length=20, choices=city_choices)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	beds = models.IntegerField()
	baths = models.DecimalField(max_digits=3, decimal_places=1)
	description = models.TextField()
	h_types = (('duplex', 'duplex'), ('apt', 'apartment'), ('house', 'house'),)
	house_type = models.CharField(max_length=10, choices=h_types)
	type_choices = (('rental', 'rental'), ('for sale', 'for sale'),)
	type = models.CharField(max_length=10, choices=type_choices)
	main_photo = models.ImageField(upload_to='photos/main-homes/')
	date = models.DateTimeField('Date Created')
	
	def contains_photo(self):
		return self.main_photo != NULL
		
	contains_photo.boolean = True
	contains_photo.short_description = 'Contains exterior photo?'
	
	
	def main_photo_thumb(self):
		if self.main_photo:
			return u'<img src="%s" />' % self.main_photo.url_125x125
		else:
			return '(No image)'

	main_photo_thumb.short_description = 'Thumb'
	main_photo_thumb.allow_tags = True
	
	def __unicode__(self):
		return self.str_addr
	
class Photo (models.Model):
	home = models.ForeignKey(Home)
	name = models.CharField(max_length = 50)
	img = models.ImageField(upload_to='photos/homes/')#+Homes.city+'/'+Homes.str_addr)
	
	def img_thumb(self):
		if self.img:
			return u'<img src="%s" />' % self.img.url_125x125
		else:
			return '(No image)'

	img_thumb.short_description = 'Thumb'
	img_thumb.allow_tags = True
	
	def __unicode__(self):
		return self.name