from django.shortcuts import render

from rest_decorator.decorators import api_view
from django.http import JsonResponse
import json
from simplecrypt import encrypt
from .models import Record
from .serializers import RecordSerializer

# Create your views here.

@api_view(["GET"])
def about(request):
    data = {
            "Name": "Abdulrahman",
            "Nickname": "rmnattas",
            "Favorite_color": "Green"
            }
    return JsonResponse(data)


@api_view(["POST"])
def encryptPost(request):
    jsonData = json.loads(request.body)
    ciphertext = encrypt(<key>, <message from jsonData>)
    record = Record(phrase=<message from jsonData>, encryptedPhrase=ciphertext)
    post.save()
    data = {'encryptedPhrase': ciphertext }
    return JsonResponse(data)





