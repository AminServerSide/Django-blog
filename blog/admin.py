from django.contrib import admin
from .models import Article , Category , Comment , Message
from . import models

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ["is_published"]
    ordering = ("title",)  # Default ordering (A-Z)
    list_display = ("title", "short_body", "is_published" , "show_image")
    search_fields = ["title" , "body"]

    def short_body(self, obj):
        return " ".join(obj.body.split()[:30]) + "..." if len(obj.body.split()) > 30 else obj.body

    short_body.short_description = "Body Preview"  # Sets the column name in admin







admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)