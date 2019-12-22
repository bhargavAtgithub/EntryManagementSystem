from django.shortcuts import render, reverse, redirect
from django.views.generic import (CreateView)
from django.http import HttpResponseRedirect
from Accounts.models import VisitorProfileInfo, RegisteredVisitorEntry
from Accounts.forms import VisitorProfileInfoForm, RegisteredVisitorEntryForm, LoginForm
from app.models import Host
from app.tasks import send_email, mail_task
# Create your views here.

class CreateVisitor(CreateView):
    form_class = VisitorProfileInfoForm
    model = VisitorProfileInfo

    def form_valid(self, form):
        self.object = form.save()
        pk = str(form.cleaned_data.get('username'))
        visitor_obj = VisitorProfileInfo.objects.get(pk = pk)
        visitor_pk = str(visitor_obj.username)
        return HttpResponseRedirect(reverse('Accounts:visitor_login'))


def CreateVisitorEntry(request,username):
    if request.method == 'POST':
        form = RegisteredVisitorEntryForm(request.POST)
        if form.is_valid():
            form.save()
            host_name = form.cleaned_data['host']
            visitor_info = VisitorProfileInfo.objects.get(pk = username)
            host_info = Host.objects.get(pk = host_name )
            host_addr = host_info.address
            visitor_name = visitor_info.name
            visitor_email = visitor_info.email
            visitor_phone = visitor_info.phone
            mail_data = {
            "host_name" : host_name,"host_addr" : host_addr,
            "visitor_name" : visitor_name,
            "visitor_mail_id" : visitor_email,
            "visitor_phone" : visitor_phone,
            "check_in_time" : form.cleaned_data.get('check_in_time'),
            "check_out_time" : form.cleaned_data.get('check_out_time')
            }
            mail_task(mail_data)
        return HttpResponseRedirect(reverse('Accounts:accounts_visitor_entry',args = (username,)))
    form_class = RegisteredVisitorEntryForm(initial={'username': username })
    return render(request,'Accounts/registeredvisitorentry_form.html',{ 'form' : form_class, 'pk' : username })


def visitor_login(request):
    form = LoginForm
    if request.method == 'POST':
        post_form = request.POST
        username = request.POST.get('username')
        password = request.POST.get('password')
        visitor_obj = VisitorProfileInfo.objects.get(pk = username)
        if visitor_obj.password == password:
            logged_in = True
            visitor_form = RegisteredVisitorEntryForm
            return HttpResponseRedirect(reverse('Accounts:accounts_visitor_entry',args = (username,)))
    return render(request,'Accounts/Login_form.html',{'form' : form})














