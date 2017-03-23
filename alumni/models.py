from __future__ import unicode_literals

from django.contrib.gis.db import models

class Alumni(models.Model):
	name = models.CharField(max_length=100)
	grad_year = models.CharField(max_length=10)
	cur_company = models.CharField(max_length=100, null=True)
	prev_company = models.CharField(max_length=100, null=True)
	projects=models.CharField(max_length=100, null=True)
	current_location = models.PointField(srid=4326)
	email = models.EmailField(null=True)
	mobile = models.CharField(max_length=50,null=True)
	
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name_plural = "alumni"
	
	