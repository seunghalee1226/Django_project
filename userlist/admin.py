from django.contrib import admin
from userlist.models import Userlist

@admin.register(Userlist)
class UserlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'email')
    list_filter = ('id', 'user_name', 'email')
    search_fields = ('id', 'user_name', 'email')
