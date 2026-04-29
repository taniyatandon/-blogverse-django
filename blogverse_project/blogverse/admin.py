from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser, BlogPost, Profile


class AppUserAdmin(UserAdmin):
    model = AppUser
    list_display = ('email', 'name', 'is_staff', 'is_superuser', 'gender', 'address', 'birthdate','phone')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone', 'address', 'gender', 'birthdate')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone', 'address', 'gender', 'password1', 'password2'),
        }),
    )

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image')
    search_fields = ('user__email', 'user__name')
    list_filter = ('user',)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','user', 'created_at')  
    search_fields = ('title', 'content')  
    list_filter = ('created_at',)  
    
admin.site.register(AppUser, AppUserAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Profile, ProfileAdmin)