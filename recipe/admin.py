from django.contrib import admin
from .models import Recipe, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "category", "created_at")
    list_filter = ("category", "author", "created_at")
    search_fields = ("title", "ingredients", "steps")
    date_hierarchy = "created_at"
