from django.contrib import admin
from .models import Pet, PetPhoto
from django.utils.html import format_html

# Register your models here.
class PetPhotoInline(admin.TabularInline):
    model = PetPhoto
    extra = 1
    readonly_fields = ['image_preview']
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 100px; border-radius: 8px;" />', obj.image.url)
        return " Нет фото"
    image_preview.short_description = 'Превью фото'

class PetAdmin(admin.ModelAdmin):
    class Media:
        js = ('pet_admin.js',)
    inlines = [PetPhotoInline]
    fieldsets = [
        (None, {"fields": ["name", "approximate_birth_date", "gender", "health_issues", "description", "status", "video"]}), ("Информация о новом владельце", {"fields": ["new_owner", "phone", "mail", "taken_date"]}),
        ("Technical information", {"fields": ["age_category"], "classes": ["collapse"]}),
    ]
    list_display = ["name", "approximate_birth_date", "age", "gender", "health_issues", "description", "status", "video"]
    search_fields = ["name"]
    readonly_fields = ["age_category"]

admin.site.register(Pet, PetAdmin)
admin.site.site_header = "meow-center.ru"
admin.site.site_title = "Панель управления"
admin.site.index_title = "Панель управления"