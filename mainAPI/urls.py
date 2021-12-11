from django.urls import path, include
from .views import *
from .models import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('Nav-Item', NavbarViewset, basename='NavItem')
router.register('Child-item', NavbarItemViewset, basename='ChildItem')
router.register('Footer', FooterViewset, basename='Footer')
router.register('Mineral-resurslar', MineralResourcesViewset, basename='MinRes')
router.register('Xaritalar', TwoMapsViewset, basename='TwoMaps')
router.register('Asosiy-maqsadlar', CompanyPurposeViewset, basename='AsosiyMaq')
router.register('Asosiy-vazifalar', CompanyTasksViewset, basename='AsosiyVazifalar')
router.register('Maqsadli-auditoriya', AuditoryViewset, basename='MaqsadliAud')
router.register('Xodimlar', StaffViewset, basename='Xodimlar')
router.register('Hujjatlar-ekspertizalari', ProjectExpertiseViewset, basename='Hujjatlar-ekspertizalari')
router.register('Yoshlar-ittifoqi', YouthUnionViewset, basename='YoshItt')
router.register('Geologik-malumot', GeoInfoViewset, basename='GeoMal')
router.register('Resurlar-bazasi', ResourceBaseViewset, basename='ResBaz')
router.register("Bolimlar", ChaptersViewset, basename="Bolimlar")
router.register("Bolimlar-element", ChaptersItemsViewset, basename="BolElem")
router.register("Offis", OfficeViewset, basename="Offis")
router.register("Qarorlar", LawsViewset, basename="Qarorlar")
router.register("Mutaxassislar-aloqasi", ProfConnectionsViewset, basename="Mutaxassislar-aloqasi")
router.register("Hisobot-qabul-qilish", ReportAcceptanceViewset, basename="Qarorlar")
router.register("Universitet-tadqiqotlari", UniversityViewset, basename="UnivTad")
router.register("Export-excel", ExcelFormViewset, basename="ExpExcel")
router.register("Yangiliklar", NewsViewset, basename="Yangiliklar")
router.register("Buhgalteriya", BookkeepingReportViewset, basename="Buhgalteriya-hisobotlari")
router.register("Ariza-manzili", ApplicationLocViewset, basename="Ariza-manzili")
router.register("Tadbirkor", BusinessmanNewsViewset, basename="Tadbirkor")
router.register("Bank-haqida", BankInfoViewset, basename="Bank-haqida")
router.register("Kon-haqida", MineInfoViewset, basename="Kon-haqida")
router.register("Material", RawMaterialViewset, basename="Material")

urlpatterns = [
    path('', include(router.urls)),
    path('download/', DownloadXmlView.as_view()),
]
