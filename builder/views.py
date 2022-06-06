from django.shortcuts import render
from builder.serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from rest_framework.parsers import JSONParser

def index(request):
    return render(request, "index.html")

@csrf_exempt
@api_view(['POST',])
def update_profile(request):
    if request.method == "POST":
        data = request.data
        profile_serializer = ProfileSerializer(data = data)
        if profile_serializer.is_valid():
            print("called here")
            profile_serializer.save()
        else:
            print(profile_serializer.errors)        
        return Response(profile_serializer.data, status = status.HTTP_201_CREATED)
