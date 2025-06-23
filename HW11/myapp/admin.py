    # myapp/admin.py

from django.contrib import admin
from .models import MyItem # Import your MyItem model

# Define a custom Admin class for MyItem
class MyItemAdmin(admin.ModelAdmin):
        """
        Customizes the display and functionality of MyItem in the Django Admin.
        """
        # 1. Custom list_display: Show two or more fields in the admin list
        #    - 'id': The primary key of the item.
        #    - 'title': The title of the item.
        #    - 'description': The description of the item.
        #    - 'created_at': The timestamp when the item was created.
        list_display = ('id', 'title', 'description', 'created_at')

        # 2. search_fields: Specify fields for searching in the Admin UI.
        #    Users can search by 'title' or 'description'.
        search_fields = ('title', 'description')

        # 3. list_filter: Specify a field for filtering the list.
        #    This creates a sidebar filter option based on the 'created_at' date.
        list_filter = ('created_at',)

        # Optional: Add fields to make them read-only in the admin edit view
        # For example, 'created_at' should not be editable by default.
        readonly_fields = ('created_at',)

    # Register your MyItem model with the custom admin class
admin.site.register(MyItem, MyItemAdmin)
