from django.contrib import admin
from studyboard.models import Studyboard

@admin.register(Studyboard)
class StudyboardAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'title', 'modify_dt')
    list_filter = ('user_name', 'title')
    search_fields = ('user_name', 'title', 'content')
    prepopulated_fields = {'slug': ('title', )}