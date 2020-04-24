from django.contrib import admin

from .models import ydl,videos
# Register your models here.
admin.site.site_header = "My WEBSITE"
admin.site.site_title = "WElcome  admin"
admin.site.index_title = "welcome to download new videos"
admin.site.register(ydl)
admin.site.register(videos)