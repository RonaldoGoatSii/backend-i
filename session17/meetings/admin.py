from django.contrib import admin
from .models import Meeting  

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Admin vê tudo
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk: # Se for uma criação nova
            obj.owner = request.user
        super().save_model(request, obj, form, change)