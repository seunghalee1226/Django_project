from django.contrib import admin
from bookmark.models import Notice, Member, StudyBoard

@admin.register(StudyBoard)
class BookmarkAdmin(admin.ModelAdmin):
    lsit_display = ('user_name', 'title', 'modify_dt')
    list_filter = ('user_name', 'title')
    search_fields = ('user_name', 'title', 'content')
    prepopulated_fields = {'slug': ('title', )}