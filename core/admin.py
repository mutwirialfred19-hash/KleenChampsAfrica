from django.contrib import admin
from django.utils.html import mark_safe
from .models import ContactInquiry

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'service_badge', 'submitted_at', 'read_status']
    list_filter = ['service', 'is_read', 'submitted_at']
    search_fields = ['full_name', 'email', 'company', 'message']
    readonly_fields = ['full_name', 'email', 'phone', 'company', 'service', 'message', 'submitted_at']
    fieldsets = (
        ('Client Details', {
            'fields': ('full_name', 'email', 'phone', 'company')
        }),
        ('Inquiry', {
            'fields': ('service', 'message', 'submitted_at')
        }),
        ('Admin', {
            'fields': ('is_read', 'notes')
        }),
    )

    @admin.display(description='Service')
    def service_badge(self, obj):
        colors = {
            'exterior': '#1a9fb5',
            'concrete': '#6b8e23',
            'floor': '#2c7a7a',
            'roof': '#1565a0',
            'waterproofing': '#7b3fa0',
            'other': '#888',
        }
        color = colors.get(obj.service, '#888')
        label = obj.get_service_display()
        html = (
            f'<span style="background:{color};color:white;padding:3px 8px;'
            f'border-radius:12px;font-size:11px">{label}</span>'
        )
        return mark_safe(html)

    @admin.display(description='Status')
    def read_status(self, obj):
        if obj.is_read:
            return mark_safe('<span style="color:green">&#10003; Read</span>')
        return mark_safe('<span style="color:#e05c00;font-weight:bold">&#9679; New</span>')

    def get_queryset(self, request):
        return super().get_queryset(request)

    actions = ['mark_as_read', 'mark_as_unread']

    @admin.action(description='Mark selected as Read')
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description='Mark selected as Unread')
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)