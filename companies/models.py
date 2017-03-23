from __future__ import unicode_literals

from django.contrib.gis.db import models


class Company(models.Model):
	name = models.CharField(max_length=200)
	speciality = models.CharField(max_length=100)
	logo = models.ImageField(upload_to='companies')
	location = models.PointField(srid=4326)
	address = models.CharField(max_length=200, null=True)
	email = models.EmailField()
	web = models.CharField(max_length=200)
	details = models.TextField()
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = "companies"
