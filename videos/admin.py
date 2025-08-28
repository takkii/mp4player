from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_published',
                    'uploaded_by', 'view_count', 'published_at')
    list_filter = ('is_published', 'category', 'created_at')
    search_fields = ('title', 'description', 'category')
    ordering = ('-created_at', )
    date_hierarchy = 'created_at'


admin.site.register(Video, VideoAdmin)
