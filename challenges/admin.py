from django.contrib import admin
from .models import Challenge

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'created_at', 'start_date', 'end_date', 'sport')
    list_filter = ('sport', 'start_date', 'end_date', 'created_at')
    search_fields = ('title', 'description', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('owner', 'title', 'description', 'sport', 'image', 'start_date', 'end_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.owner_id:
            obj.owner = request.user
        obj.save()

admin.site.register(Challenge, ChallengeAdmin)
