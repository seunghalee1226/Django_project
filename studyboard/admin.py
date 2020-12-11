from django.contrib import admin
from studyboard.models import Studyboard

@admin.register(Studyboard)
class StudyboardAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'title', 'modify_dt', 'tag_list')
    list_filter = ('user_name', 'title')
    search_fields = ('user_name', 'title', 'content')
    prepopulated_fields = {'slug': ('title', )}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())
