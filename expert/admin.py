from django.contrib import admin
from . models import Expert
from django_summernote.admin import SummernoteModelAdmin
@admin.register(Expert)
class ExpertAdmin(SummernoteModelAdmin):
    summernote_fileds = ('body',)
    list_display = (
        'title',
        'writer',
        'pub_date',
        'body',
        'image',

    )
    list_display_links = list_display


# class PhotoInline(admin.TabularInline):
#     model = Image

# class ExpertAdmin(admin.ModelAdmin):
#     inlines = [PhotoInline, ]

# admin.site.register(Expert, ExpertAdmin)

