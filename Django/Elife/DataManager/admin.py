from django.contrib import admin
from DataManager.models import Audio,User,UserAudioBehavior,Word

# Register your models here.

class AudioAdmin(admin.ModelAdmin):
    list_display = ('audioTitle','audioId','audioType','audioDate')

class UserAdmin(admin.ModelAdmin):
    list_display = ('userId','userCorrectRate')

class UserAudioBehaviorAdmin(admin.ModelAdmin):
    list_display = ('userId','audioId','isCollected','audioCorrectRate')

class WordAdmin(admin.ModelAdmin):
    list_display = ('wordId','word')

admin.site.register(Audio,AudioAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(UserAudioBehavior,UserAudioBehaviorAdmin)
admin.site.register(Word,WordAdmin)