from django.contrib import admin
from staff.models import StaffProfile


class StaffProfile(admin.ModelAdmin):

    admin.site.register(StaffProfile)




