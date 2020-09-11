from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    search_fields = ['first_name', 'last_name']
    list_display = ('first_name', 'last_name',)
    filter_horizontal = ('groups', 'user_permissions')
    ordering = ('last_name',)
    fieldsets = (
        ('Last Name', {'fields': ('last_name', 'first_name', 'password', 'avatar')}),
        ('Email', {'fields': ('email',)}),
        ('Other', {'fields': (
            'position',
            'is_active',
            'is_staff',
            'is_superuser',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'is_teamlead', 'is_director', 'avatar')}
         ),
    )


admin.site.register(User, UserAdmin)
