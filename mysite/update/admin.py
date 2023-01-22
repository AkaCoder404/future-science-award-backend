from django.contrib import admin

# Register your models here.
from .models import MyUser, MyUserUploads

# admin display
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "affiliation", "email", "category", "research", "contribution", 'get_files')

    def get_files(self, obj):
        return [x.filename for x in obj.myuseruploads_set.all()]
    get_files.admin_order_field = 'myuseruploads'
    get_files.short_description = 'letters'
    

@admin.register(MyUserUploads)
class MyUserAdminUploads(admin.ModelAdmin):
    list_display = ("id", "filename", "file", "uploadTime", "get_user")

    def get_user(self, obj):
        return obj.myuser.name
    get_user.admin_order_field = 'myuser'
    get_user.short_description = 'myuser name'