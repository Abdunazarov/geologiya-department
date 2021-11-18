from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from utils.download_file import download


class NavbarViewset(viewsets.ModelViewSet):
    serializer_class = NavbarSerializer
    queryset = Navbar.objects.all()


class NavbarItemViewset(viewsets.ModelViewSet):
    serializer_class = NavbarItemSerializer
    queryset = NavbarItem.objects.all()


class FooterViewset(viewsets.ModelViewSet):
    serializer_class = FooterSerializer
    queryset = Footer.objects.all()


class MineralResourcesViewset(viewsets.ModelViewSet):
    serializer_class = MineralResourcesSerializer
    queryset = MineralResources.objects.all()


class TwoMapsViewset(viewsets.ModelViewSet):
    serializer_class = TwoMapsSerializer
    queryset = TwoMaps.objects.all()


class CompanyPurposeViewset(viewsets.ModelViewSet):
    serializer_class = CompanyPurposeSerializer
    queryset = CompanyPurpose.objects.all()


class CompanyTasksViewset(viewsets.ModelViewSet):
    serializer_class = CompanyTasksSerializer
    queryset = CompanyTasks.objects.all()


class CompanyTasksItemsViewset(viewsets.ModelViewSet):
    serializer_class = CompanyTasksItemsSerializer
    queryset = CompanyTasksItems.objects.all()


class AuditoryViewset(viewsets.ModelViewSet):
    serializer_class = AuditorySerializer
    queryset = Auditory.objects.all()


class StaffViewset(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class ProjectExpertiseViewset(viewsets.ModelViewSet):
    serializer_class = ProjectExpertiseSerializer
    queryset = ProjectExpertise.objects.all()


class YouthUnionViewset(viewsets.ModelViewSet):
    serializer_class = YouthUnionSerializer
    queryset = YouthUnion.objects.all()


class GeoInfoViewset(viewsets.ModelViewSet):
    serializer_class = GeoInfoSerializer
    queryset = GeoInfo.objects.all()


class ResourceBaseViewset(viewsets.ModelViewSet):
    serializer_class = ResourceBaseSerializer
    queryset = ResourceBase.objects.all()


class ChaptersViewset(viewsets.ModelViewSet):
    serializer_class = ChaptersSerializer
    queryset = Chapters.objects.all()


class ChaptersItemsViewset(viewsets.ModelViewSet):
    serializer_class = ChaptersItemsSerializer
    queryset = ChaptersItems.objects.all()


class OfficeViewset(viewsets.ModelViewSet):
    serializer_class = OfficeSerializer
    queryset = Office.objects.all()


class LawsViewset(viewsets.ModelViewSet):
    serializer_class = LawsSerializer
    queryset = Laws.objects.all()


class ProfConnectionsViewset(viewsets.ModelViewSet):
    serializer_class = ProfConnectionsSerializer
    queryset = ProfConnections.objects.all()


class ReportAcceptanceViewset(viewsets.ModelViewSet):
    serializer_class = ReportAcceptanceSerializer
    queryset = ReportAcceptance.objects.all()


class UniversityViewset(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()


class ExcelFormViewset(viewsets.ModelViewSet):
    serializer_class = ExcelFormSerializer
    queryset = ExcelForm.objects.all()


class NewsViewset(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class BookkeepingReportViewset(viewsets.ModelViewSet):
    serializer_class = BookkeepingReportSerializer
    queryset = BookkeepingReport.objects.all()


class MineInfoViewset(viewsets.ModelViewSet):
    serializer_class = MineInfoSerializer
    queryset = MineInfo.objects.all()


class BusinessmanNewsViewset(viewsets.ModelViewSet):
    serializer_class = BusinessmanSerializer
    queryset = Businessman.objects.all()


class ApplicationLocViewset(viewsets.ModelViewSet):
    serializer_class = ApplicationLocSerializer
    queryset = ApplicationLoc.objects.all()


class BankInfoViewset(viewsets.ModelViewSet):
    serializer_class = BankInfoSerializer
    queryset = BankInfo.objects.all()


class DownloadXmlView(APIView):

    def get(self, url, *args, **kwargs):
        district_dt = int(url.GET.get("viloyat", 0))
        road_district_rd = int(url.GET.get("road_district", 0))
        plant_pt = int(url.GET.get("plant", 0))
        pitomnik_plants = ExcelForm.objects.all()
        _list_pitomnikdb = []

        for x in pitomnik_plants:
            _list_pitomnikdb.append(
                tuple((str(x.condition_a_b_c1),
                       str(x.dist) + " " + str(x.number_explot),
                       "(" + str(int(x.condition_a_b_c2)) + "-" + str(int(x.condition_c2)) + ")km -" + str(x.location),
                       str(x.id),
                       str(x.raw_material),
                       str(x.region))))

        path = "main"
        row_start_index = 8
        column_start_index = 6
        column_end_range = 11
        indexing = True
        db = list(_list_pitomnikdb)
        print(_list_pitomnikdb, "_list_pitomnik")
        print(path, "path")
        print(row_start_index, "start row")
        print(column_start_index)
        print(column_end_range, "end column")
        print(indexing, 'indexing')
        return download(
            _list_pitomnikdb,
            path,
            row_start_index,
            column_start_index,
            column_end_range,
            indexing,
        )