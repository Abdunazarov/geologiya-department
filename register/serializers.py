from rest_framework.serializers import Serializer, ModelSerializer
from django.contrib.auth import get_user_model


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
