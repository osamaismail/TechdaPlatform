from django.contrib import admin
from .models import Activity, Attend, Volunteer



class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'actType', 'instructor', 'actDate')


admin.site.register(Activity, ActivityAdmin)

