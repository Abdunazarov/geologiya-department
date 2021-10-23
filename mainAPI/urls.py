from django.contrib import admin
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
router.register('Asosiy-vazifalar-element', CompanyTasksItemsViewset, basename='AsosiyVazifalarElem')
router.register('Maqsadli-auditoriya', AuditoryViewset, basename='MaqsadliAud')
router.register('Xodimlar', StaffViewset, basename='Xodimlar')
router.register('Hujjatlar-ekspertizalari', ProjectExpertiseViewset, basename='Hujjatlar-ekspertizalari')
router.register('Yoshlar-ittifoqi', YouthUnionViewset, basename='YoshItt')
urlpatterns = [
    path('', include(router.urls)),
]
