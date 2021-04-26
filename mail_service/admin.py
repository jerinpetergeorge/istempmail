from django.contrib import admin

from mail_service import models


class AbstractDomainAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user")
    list_display_links = ("name",)


admin.site.register(models.BlackListDomain, AbstractDomainAdmin)
admin.site.register(models.WhiteListDomain, AbstractDomainAdmin)
