import openpyxl

from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.download_file import download
from rest_framework.permissions import AllowAny
from openpyxl import Workbook


class NavbarViewset(viewsets.ModelViewSet):
    serializer_class = NavbarSerializer
    queryset = Navbar.objects.all()
    authentication_classes = []
    permission_classes = [AllowAny]


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
    permission_classes = [AllowAny]
    authentication_classes = []


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


class RawMaterialViewset(viewsets.ModelViewSet):
    serializer_class = RawMaterialSerializer
    queryset = RawMaterial.objects.all()


class DownloadXmlView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, url, *args, **kwargs):
        excel_objects = ExcelForm.objects.all()
        list_excel = []

        list_raws = list_sub = final_list = []

        for excel in excel_objects:
            raw = excel.sub_raw_material.parent.rawmaterial
            sub = excel.sub_raw_material.submaterial

            list_sub.append(sub)
            list_raws.append(raw)

            if sub not in list_sub and raw not in list_raws:
                obj = tuple((raw, sub))
                final_list.append(obj)

        for x in excel_objects:
            list_excel.append(
                tuple((
                    str(x.location),
                    str(x.condition_a_b_c1),
                    str(x.condition_c2),
                    str(x.absorption_level),
                    str(x.license),
                    str(x.income_2019),
                    str(x.affiliation),
                    str(f"{x.affirmation_year}, {x.protocol_num}"),
                    str(x.prod_quantity),
                    str(x.region),
                ))
            )

        print(final_list)
        path = "mn"
        row_start_index = 8

        column_start_index = 2
        column_end_range = 11
        indexing = True

        return download(
            list_excel,
            path,
            row_start_index,
            column_start_index,
            column_end_range,
            indexing,
            final_list
        )

