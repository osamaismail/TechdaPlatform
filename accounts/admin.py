from django.contrib import admin
from .models import UserProfile



class UserLevelAdmin(admin.ModelAdmin):
    list_display = ('gender', 'user', 'type', 'age')


admin.site.register(UserProfile, UserLevelAdmin)
