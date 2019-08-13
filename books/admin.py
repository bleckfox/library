from django.contrib import admin
from .models import Books, HelpfulResources
# Register your models here.
admin.site.register(Books)
admin.site.register(HelpfulResources)