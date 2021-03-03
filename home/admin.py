from django.contrib import admin
from home.models import UserAccount
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = UserAccount
    search_fields = ('email',)
    list_filter = ('email', 'is_active', 'is_staff')
    ordering = ('email',)
    list_display = ('email',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(UserAccount, UserAdminConfig)

