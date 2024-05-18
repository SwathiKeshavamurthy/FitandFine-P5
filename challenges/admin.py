from django.contrib import admin
from .models import Challenge

class ChallengeAdmin(admin.ModelAdmin):
    """
    Custom admin for the Challenge model.
    """
    list_display = ('title', 'owner', 'sport', 'start_date', 'end_date', 'created_at')
    list_filter = ('sport', 'start_date', 'end_date', 'created_at')
    search_fields = ('title', 'description', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set owner during the first save.
            obj.owner = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
        Limit the visibility of the challenges to the ones created by the logged-in admin.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def has_change_permission(self, request, obj=None):
        """
        Only allow the owner or superuser to change the object.
        """
        if obj and (obj.owner != request.user and not request.user.is_superuser):
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        """
        Only allow the owner or superuser to delete the object.
        """
        if obj and (obj.owner != request.user and not request.user.is_superuser):
            return False
        return super().has_delete_permission(request, obj)


admin.site.register(Challenge, ChallengeAdmin)
