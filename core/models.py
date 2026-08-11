from django.db import models

class ContactInquiry(models.Model):
    SERVICE_CHOICES = [
        ('exterior', 'Building Exterior Restoration'),
        ('concrete', 'Outdoor Concrete Restoration & Resurfacing'),
        ('floor', 'Floor Care & Interior Walls Restoration'),
        ('roof', 'Tiled Roof Cleaning & Maintenance'),
        ('waterproofing', 'Waterproofing & Protective Coating'),
        ('other', 'Other / Not Sure Yet'),
    ]

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=200, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='other')
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notes = models.TextField(blank=True, help_text="Internal notes (admin only)")

    class Meta:
        verbose_name = "Client Inquiry"
        verbose_name_plural = "Client Inquiries"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.full_name} — {self.get_service_display()} ({self.submitted_at.strftime('%d %b %Y')})"
