from django.contrib import admin
from . models import Expert, Photo
class PhotoInline(admin.TabularInline):
    model = Photo

class ExpertAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]

admin.site.register(Expert, ExpertAdmin)

