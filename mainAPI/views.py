from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from utils.download_file import download
from rest_framework.permissions import AllowAny


class NavbarViewset(viewsets.ModelViewSet):
    serializer_class = NavbarSerializer
    queryset = Navbar.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = []


class NavbarItemViewset(viewsets.ModelViewSet):
    serializer_class = NavbarItemSerializer
    queryset = NavbarItem.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = []


class FooterViewset(viewsets.ModelViewSet):
    serializer_class = FooterSerializer
    queryset = Footer.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = []


class MineralResourcesViewset(viewsets.ModelViewSet):
    serializer_class = MineralResourcesSerializer
    queryset = MineralResources.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = []



class TwoMapsViewset(viewsets.ModelViewSet):
    serializer_class = TwoMapsSerializer
    queryset = TwoMaps.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = []


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
    permission_classes = [AllowAny]
    authentication_classes = []


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
    permission_classes = [AllowAny]
    authentication_classes = []


class BookkeepingReportViewset(viewsets.ModelViewSet):
    serializer_class = BookkeepingReportSerializer
    queryset = BookkeepingReport.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = []


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


from openpyxl import Workbook


class DownloadXmlView(APIView):

    def get(self, url, *args, **kwargs):
        excel_objects = ExcelForm.objects.all()
        list_excel = []

        obj_quantity = len(ExcelForm.objects.all())

        for x in excel_objects:
            list_excel.append(
                tuple((
                     str(x.location),
                     str(x.condition_a_b_c1),
                     str(x.condition_c2),
                     # str(x.condition_a_b_c2),
                     str(x.absorption_level),
                     str(x.license),
                     str(x.income_2019),
                     str(x.affiliation),
                     # str(x.exploitation),
                     str(f"{x.affirmation_year}, {x.protocol_num}"),
                     # str(x.number_explot),
                     str(x.prod_quantity),
                     # str(x.protocol_num),
                     # str(x.raw_material),
                     str(x.region),
                     # str(x.dist),
                    )))

        path = "mn"
        row_start_index = 8

        # for x in range(0, obj_quantity):  # (0, 2)
        #     if x == 0:
        #         continue
        #     elif x % 2 == 0 or x == 1:
        #         row_start_index += 1
        #     else:
        #         row_start_index += 2

        column_start_index = 2
        column_end_range = 11
        indexing = True
        db = list(list_excel)

        return download(
            list_excel,
            path,
            row_start_index,
            column_start_index,
            column_end_range,
            indexing,
        )


