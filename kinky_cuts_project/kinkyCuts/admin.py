from django.contrib import admin
from kinkyCuts.models import UserProfile, Rating, Creation

class creationAdmin(admin.ModelAdmin):
    list_display =  ['user', 'imageID', 'picture', 'likes', 'creationDate']

class ratingsAdmin(admin.ModelAdmin):
    list_display = ['user', 'imageID']

admin.site.register(UserProfile)
admin.site.register(Rating, ratingsAdmin)
admin.site.register(Creation, creationAdmin)
