from django.contrib import admin
from Accounts.models import RegisteredVisitorEntry, VisitorProfileInfo
# Register your models here.

admin.site.register(RegisteredVisitorEntry)
admin.site.register(VisitorProfileInfo)