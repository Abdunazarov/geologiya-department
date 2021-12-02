import datetime
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import CustomUserSerializer


class RegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        data['password'] = data['token']
        serialize = CustomUserSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            tk = Token.objects.create(user_id=serialize.data['id'], key=data['token'])
            tk.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)


class ApiToken(APIView):
    def post(self, request):
        user = get_user_model()
        email = request.data.get('email')

        try:
            user.objects.get(email=email)
            return Response({'data': {'status': 'error', 'cause': f'{email} already exists'}})

        except ObjectDoesNotExist:
            return Response({"status": "ok"})