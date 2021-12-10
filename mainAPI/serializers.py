from rest_framework import serializers
from .models import *



class NavbarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarItem
        exclude = ['status']


class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = '__all__'


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'


class MineralResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MineralResources
        fields = '__all__'


class TwoMapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwoMaps
        fields = '__all__'


class CompanyPurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPurpose
        fields = '__all__'


class CompanyTasksItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTasksItems
        fields = '__all__'


class CompanyTasksSerializer(serializers.ModelSerializer):
    company_tasks_items = CompanyTasksItemsSerializer(read_only=True, many=True)

    class Meta:
        model = CompanyTasks
        fields = '__all__'


class AuditorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditory
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class ProjectExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class YouthUnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouthUnion
        fields = '__all__'


class GeoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoInfo
        fields = '__all__'


class ResourceBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceBase
        fields = '__all__'


class ChaptersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = '__all__'


class ChaptersItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChaptersItems
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class LawsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laws
        fields = '__all__'


class ProfConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfConnections
        fields = '__all__'


class ReportAcceptanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportAcceptance
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class ExcelFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelForm
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class BookkeepingReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookkeepingReport
        fields = '__all__'


class MineInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MineInfo
        fields = '__all__'


class BankInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankInfo
        fields = '__all__'


class ApplicationLocSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationLoc
        fields = '__all__'


class BusinessmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businessman
        fields = '__all__'


class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'
