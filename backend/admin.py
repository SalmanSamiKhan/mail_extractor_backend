# ******** 1 ********
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     list_display = ('company_name', 'username', 'email', 'subscription_start', 'subscription_end', 'is_active')
#     list_filter = ('is_active', 'subscription_start', 'subscription_end')
#     search_fields = ('company_name', 'username', 'email')
#     ordering = ('company_name',)
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('email', 'name', 'address', 'company_name')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined', 'subscription_start', 'subscription_end')}),
#     )

# admin.site.register(CustomUser, CustomUserAdmin)

# ********* 2 *********

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.utils.html import format_html
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     list_display = ('company_name', 'username', 'email', 'subscription_start', 'subscription_end', 'is_active_switch', 'edit_user')
#     list_filter = ('is_active', 'subscription_start', 'subscription_end')
#     search_fields = ('company_name', 'username', 'email')
#     ordering = ('company_name',)

#     def is_active_switch(self, obj):
#         return format_html('<input type="checkbox" {} onclick="toggle_user_active(this)" data-id="{}">',
#                            'checked' if obj.is_active else '', obj.id)

#     is_active_switch.short_description = 'Is Active'

#     def edit_user(self, obj):
#         return format_html('<a href="{}">Edit</a>', f'/admin/backend/customuser/{obj.id}/change/')

#     edit_user.short_description = 'Edit User'

# admin.site.register(CustomUser, CustomUserAdmin)


# ********** 3 *********

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        'company_name',
        'username',
        'email',
        'subscription_start',
        'subscription_end',
        'is_active',
        'edit_user_link',
    )
    list_filter = ('is_active', 'subscription_start', 'subscription_end')
    search_fields = ('company_name', 'username', 'email')
    ordering = ('company_name',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'name', 'address', 'company_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'subscription_start', 'subscription_end')}),
    )

    def edit_user_link(self, obj):
        change_url = reverse('admin:backend_customuser_change', args=[obj.id])
        return format_html('<a href="{}">Edit</a>', change_url)

    edit_user_link.short_description = 'Edit User'

admin.site.register(CustomUser, CustomUserAdmin)


