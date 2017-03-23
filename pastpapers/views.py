from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from pastpapers.models import Paper


class PastpaperView(TemplateView):
	template_name = 'pastpapers.html'


def first_year(request):
	papers = Paper.objects.filter(year='first-year')
	return render(request, 'first_year.html', {'papers': papers})


def second_year(request):
	papers = Paper.objects.filter(year='second-year')
	return render(request, 'second_year.html', {'papers': papers})


def third_year(request):
	papers = Paper.objects.filter(year='third-year')
	return render(request, 'third_year.html', {'papers': papers})


def fourth_year(request):
	papers = Paper.objects.filter(year='fourth-year')
	return render(request, 'fourth_year.html', {'papers': papers})


def fifth_year(request):
	papers = Paper.objects.filter(year='fifth-year')
	return render(request, 'fifth_year.html', {'papers': papers})


def paper_detail(request, id, slug):
	paper = get_object_or_404(Paper, id=id, slug=slug)
	return render(request, 'paper_detail.html', {'paper': paper})
