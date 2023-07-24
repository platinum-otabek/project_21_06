from django.contrib import admin
from .models import BookCategoryModel,BookModel,AuthorModel
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    # Specify the model and the fields to be displayed in the admin panel
    model = CustomUser
    list_display = ('username', 'email', 'roles', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'roles')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'roles', 'is_staff', 'is_active')

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(AuthorModel)
admin.site.register(BookCategoryModel)