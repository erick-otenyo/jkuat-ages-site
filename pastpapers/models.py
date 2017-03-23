from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Paper(models.Model):
	COURSE_CHOICES = (
		('GIS', 'GIS'),
		('GEGIS', 'GEGIS')
	)
	UNIT_CHOICES = (
		('Calculus I', 'Calculus 1'),
		('Calculus II', 'Calculus 2'),
		('Calculus III', 'calculus 3'),
		('Calculus IV', 'calculus 4'),
	)
	CODE_CHOICES = (
		('SMA 2270', 'SMA 2270'),
		('EGS 2304', 'EGS 2304'),
	)
	YEAR_CHOICES = (
		('first-year','First Year'),
		('second-year','Second Year'),
		('third-year','Third Year'),
		('fourth-year','Fourth Year'),
		('fifth-year','Fifth Year'),
	)
	SEM_CHOICES = (
		('1','1'),
		('2','2'),
	)
	course = models.CharField(max_length=10, choices=COURSE_CHOICES)
	year = models.CharField(max_length=50,choices=YEAR_CHOICES)
	semester = models.CharField(max_length=5,choices=SEM_CHOICES)
	date = models.CharField(max_length=10)
	unit_title = models.CharField(max_length=100,choices=UNIT_CHOICES)
	unit_code = models.CharField(max_length=50,choices=CODE_CHOICES)
	image = models.ImageField(upload_to='pastpapers')
	slug = models.SlugField()
	
	def __unicode__(self):
		return self.year + self.course + self.unit_title

	def get_absolute_url_1(self):
		return reverse('paper_detail_1', args=[self.id,self.slug])
	def get_absolute_url_2(self):
		return reverse('paper_detail_2', args=[self.id,self.slug])
	def get_absolute_url_3(self):
		return reverse('paper_detail_3', args=[self.id,self.slug])
	def get_absolute_url_4(self):
		return reverse('paper_detail_4', args=[self.id,self.slug])
	def get_absolute_url_5(self):
		return reverse('paper_detail_5', args=[self.id,self.slug])
