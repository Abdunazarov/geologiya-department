from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model


class RegisterView(APIView):

    def post(self, request):
        data = request.data
        print(data)
        user = get_user_model().objects.create(email=data['email'], username=data['email'])
        user.set_password(data['key'])
        user.save()
        Token.objects.create(user=user, key=data['key'])
        return Response(status=200)