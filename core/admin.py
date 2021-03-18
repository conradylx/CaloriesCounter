from django.contrib import admin

from core.models import Item

class ItemAdmin(admin.ModelAdmin):
    class Meta:
        model = Item
    list_filter = ['name']
    list_display = ['name']

admin.site.register(Item, ItemAdmin)
