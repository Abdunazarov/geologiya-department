from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group
from .models import *


admin.site.register(Navbar)
admin.site.register(NavbarItem)
admin.site.register(Footer)
admin.site.register(MineralResources)
admin.site.register(TwoMaps)
admin.site.register(CompanyPurpose)
admin.site.register(CompanyTasks)
admin.site.register(CompanyTasksItems)
admin.site.register(Auditory)
admin.site.register(Staff)
admin.site.register(ProjectExpertise)
admin.site.register(YouthUnion)
admin.site.register(ResourceBase)
admin.site.register(GeoInfo)
admin.site.register(Chapters)
admin.site.register(ChaptersItems)
admin.site.register(Office)
admin.site.register(Laws)
admin.site.register(ProfConnections)
admin.site.register(ReportAcceptance)
admin.site.register(University)


admin.site.site_header = "Geologiya Axborot Markazi"

# admin.site.register(MyAdmin)
admin.site.unregister(Group)
admin.site.site_title = "Geology"
admin.site.index_title = "Welcome to 'Geologia Axborot Markazi'"

