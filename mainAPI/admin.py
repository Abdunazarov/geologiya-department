from django.contrib import admin
from .models import *
from .models import models
from .forms import AdminApplicationForm


class ApplicationLocAdmin(admin.ModelAdmin):
    form = AdminApplicationForm
    # def region_tag(self, obj):
    #     return obj.region.raw_materials
    #
    # def raw_material_tag(self, obj):
    #     return obj.details.raw_material
    #
    # # list_display = ('region_tag', 'raw_material_tag')
    # list_select_related = ('region', )


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
admin.site.register(ExcelForm)
admin.site.register(BookkeepingReport)
admin.site.register(News)
admin.site.register(BankInfo)
admin.site.register(ApplicationLoc, ApplicationLocAdmin)
admin.site.register(MineInfo)
admin.site.register(Businessman)


