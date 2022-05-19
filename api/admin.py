from django.contrib import admin

from api.models import VersionDescription, VersionDescriptionHtml, VersionMinecraft

admin.site.register(VersionMinecraft)
admin.site.register(VersionDescriptionHtml)
admin.site.register(VersionDescription)