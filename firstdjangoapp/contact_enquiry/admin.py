from django.contrib import admin
from contact_enquiry.models import ContactEnquiry

class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

admin.site.register(ContactEnquiry, ContactEnquiryAdmin)
# Register your models here.
