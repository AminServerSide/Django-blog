from django.contrib import admin
from .models import Article, Category, Comment, Message , Like
from . import models

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ["is_published"]
    ordering = ("title",)  # Default ordering (A-Z)
    list_display = ("title", "short_body", "is_published", "show_image")
    search_fields = ["title", "body"]

    def short_body(self, obj):
        return " ".join(obj.body.split()[:30]) + "..." if len(obj.body.split()) > 30 else obj.body

    short_body.short_description = "Body Preview"  # Sets the column name in admin


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ("title",)
    list_display = ("title",)
    search_fields = ["title"]

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    ordering = ("created",)  # Sorting by the comment's creation date
    list_display = ("article", "user", "short_body", "created")
    search_fields = ["user", "body"]

    def short_body(self, obj):
        return " ".join(obj.body.split()[:30]) + "..." if len(obj.body.split()) > 30 else obj.body

    short_body.short_description = "Comment Preview"

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    ordering = ("date",)  # Sorting by the 'date' field
    list_display = ("title", "email", "short_text", "date", "created")
    search_fields = ["title", "email", "text"]

    def short_text(self, obj):
        return " ".join(obj.text.split()[:30]) + "..." if len(obj.text.split()) > 30 else obj.text

    short_text.short_description = "Text Preview"


admin.site.register(models.Like)