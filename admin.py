from django.contrib import admin

from commentApp.models import Comments, Articles

admin.site.register(Articles)
admin.site.register(Comments)
