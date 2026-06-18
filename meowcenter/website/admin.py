from django.contrib import admin
from .models import Pet

# Register your models here.
class PetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "age", "gender", "health_issues", "description", "status", "photo", "video"]}),
        ("Date information", {"fields": ["created_at"], "classes": ["collapse"]}),
    ]
    list_display = ["name", "age", "gender", "health_issues", "description", "status", "photo", "video"]
    list_filter = ["created_at"]
    search_fields = ["name"]
    readonly_fields = ["created_at"]

admin.site.register(Pet, PetAdmin)