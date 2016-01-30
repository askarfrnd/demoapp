from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.views.generic import View, TemplateView

from .forms import LogForm


class HomePage(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return {'form': LogForm()}


class WelcomePage(View):

    def get(self, request):
        return HttpResponseRedirect('/')

    def post(self, request):
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'name': request.POST['name']
                       }
            return render_to_response('welcome.html', context,  RequestContext(request))
        return HttpResponseRedirect('/')
