from django.contrib import admin
from notice.models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'title', 'modify_dt')
    list_filter = ('user_name', 'title')
    search_fields = ('user_name', 'title', 'content')
    prepopulated_fields = {'slug': ('title', )}