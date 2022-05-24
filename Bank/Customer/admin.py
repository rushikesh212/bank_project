from django.contrib import admin
from .models import Data


# Register your models here.

class DataAdmin(admin.ModelAdmin):
    data_list = ['name', 'account_no', 'location', 'mobile_no']


admin.site.register(Data, DataAdmin)
