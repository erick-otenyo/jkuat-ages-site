from django.shortcuts import render, get_object_or_404

from activities.models import Activity


def activities_list(request):
	activities = Activity.objects.all().order_by('-date')
	return render(request, 'activities.html', {'activities': activities})


def activity_detail(request, pk, slug):
	activity = get_object_or_404(Activity, pk=pk, slug=slug)
	return render(request, 'activity_detail.html', {'activity': activity})
