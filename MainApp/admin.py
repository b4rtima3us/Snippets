from django.contrib import admin
from MainApp.models import Snippet
# Register your models here.

# Example 1
# admin.site.register(Snippet)


# Example 2
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['name', 'lang', 'creation_date', 'code']
