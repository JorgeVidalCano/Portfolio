from django.contrib.auth.models import Group
from django.contrib import admin
from .models import *

admin.site.unregister(Group)

class CommonFunctions():
    def has_add_permission(self, request, obj=None):
        # The add button disapear when there is one.
        if self.objects.all().count() == 1:
            return False
        else:
            return True

@admin.register(MetaData)
class MetaAdmin(CommonFunctions, admin.ModelAdmin):
    list_display = ['metaDescription', 'metaKeywords']
    def has_add_permission(self, request, obj=None):
        super() 

@admin.register(HomeData)
class HomeAdmin(admin.ModelAdmin, CommonFunctions):
    list_display = ['mainName', 'description']
    def has_add_permission(self, request, obj=None):
        super() 