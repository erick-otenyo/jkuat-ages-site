from django.views.generic import TemplateView


class HomeView(TemplateView): template_name = 'index.html'


class ControlsView(TemplateView): template_name = 'controls.html'


class AlumniView(TemplateView): template_name = 'alumni.html'
