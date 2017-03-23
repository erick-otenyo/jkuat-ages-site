from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.core.urlresolvers import reverse

APP_NAME = 'activities'

class Activity(models.Model):
	CAT_CHOICES = (
		('normal','normal'),
		('notice','notice'),
	)
	name = models.CharField(max_length=200)
	date = models.DateField()
	image = models.ImageField(upload_to='activities/%Y/%m/%d')
	detail = models.TextField()
	location = models.PointField(srid=4326, null=True,blank=True)
	slug = models.SlugField(max_length=50,unique_for_date='date')
	category = models.CharField(max_length=100, choices=CAT_CHOICES)
	
	def __unicode__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('activity_detail', args=[self.slug,self.id])
	
	class Meta:
		verbose_name_plural = "activities"
	
	