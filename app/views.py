from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        data = dict()
        data['refresh'] = str(token)
        data['access'] = str(token.access_token)
        # self.request.session['sname'] = 'irfan'  
        # response.set_cookie('access', token.access_token)

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    print(user.username)
    return Response("serializer.data")