from django.shortcuts import render
from django.http import HttpResponse
import requests


def users(request):
    response = requests.get('https://hapi.fhir.org/baseR4/CarePlan/49011')
    data = response.json()
    return render(request, "users.html", {'data': data})