from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class Info(APIView):
    def get(self, request, *args, **kwargs):
        data ={
            'Slackusername' : "Bolaji",
            'backend' : True,
            'age' : 25,
            'bio' : "I'm bolaji i love to code and play football"
        }
        return Response(data)