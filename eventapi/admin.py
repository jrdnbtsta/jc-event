from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from eventapi.models import UserInfo, Message, Announcement, Todo, KauaiSuggestion
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


class AnnouncementAdmin(admin.ModelAdmin):
    pass


class TodoAdmin(admin.ModelAdmin):
    pass


class KauaiSuggestionAdmin(admin.ModelAdmin):
    pass



admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(KauaiSuggestion, KauaiSuggestionAdmin)
