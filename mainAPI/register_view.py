import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token


class RegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        print(data)
        user = get_user_model().objects.create(email=data['email'], username=data['email'])
        user.set_password(data['token'])
        user.save()
        tk = Token.objects.create(user_id=user.id, key=data['token'])
        tk.save()
        return Response(status=200, data={'key': tk.key})


class ApiToken(APIView):
    def post(self, request):
        user = get_user_model()
        email = request.data.get('email')

        try:
            user.objects.get(email=email)
            return Response({'data': {'status': 'error', 'cause': f'{email} already exists'}})

        except:
            return Response({"status": "ok"})