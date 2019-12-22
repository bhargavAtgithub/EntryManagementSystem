from django.shortcuts import render, redirect
from django.utils import timezone
from app.models import Host, VisitorEntry
from app.forms import HostForm, VisitorEntryForm
from django.views.generic import (CreateView, TemplateView)
from django.http import HttpResponseRedirect
from .tasks import mail_task

# Create your views here.

class AboutView(TemplateView):
    template_name = 'app/about.html'

class CreateVisitorEntry(CreateView):
    form_class = VisitorEntryForm
    model = VisitorEntry

    def form_valid(self, form):
        self.object = form.save()
        host_name = form.cleaned_data['host']
        host_obj = Host.objects.get(pk = host_name)
        host_addr = host_obj.address
        mail_data = {
        "host_name" : host_name,"host_addr" : host_addr,
        "visitor_name" : form.cleaned_data.get('name'),
        "visitor_mail_id" : form.cleaned_data.get('email'),
        "visitor_phone" : form.cleaned_data.get('phone'),
        "check_in_time" : form.cleaned_data.get('check_in_time'),
        "check_out_time" : form.cleaned_data.get('check_out_time')
        }

        mail_task(mail_data)
        return HttpResponseRedirect(self.get_success_url())

class CreateHost(CreateView):
    form_class = HostForm
    model = Host

