from django.contrib import admin
from gushi.models import User, AudioInfo_User, AudioInfo


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
admin.site.register(User, UserAdmin)


class AudioInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'date')
admin.site.register(AudioInfo, AudioInfoAdmin)


class AudioInfo_UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'audioInfo', 'id')
admin.site.register(AudioInfo_User, AudioInfo_UserAdmin)



