from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "client",
        "created_by",
        "created_at",
    )

    search_fields = (
        "title",
        "client__company_name",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20