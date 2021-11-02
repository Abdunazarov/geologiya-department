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


class CompanyTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTasks
        fields = '__all__'


class CompanyTasksItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTasksItems
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


