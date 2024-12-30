from django.contrib import admin
from contacts.models import User, Contact


# Register your models here.
admin.site.register(User)
admin.site.register(Contact)