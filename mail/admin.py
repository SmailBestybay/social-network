from django.contrib import admin
from .models import Email, User

@admin.action(description='Mark selected emails read')
def make_read(modeladmin, request, queryset):
    queryset.update(read=True)

@admin.action(description='Mark selected emails unread')
def make_unread(modeladmin, request, queryset):
    queryset.update(read=False)

class MailAdmin(admin.ModelAdmin):
    list_filter = ('read',)
    list_display = ['user', 'sender','subject', 'read']
    actions = [make_read, make_unread]

# Register your models here.
admin.site.register(User)
admin.site.register(Email, MailAdmin)