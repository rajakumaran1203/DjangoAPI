from django.shortcuts import render
from django.views.generic import TemplateView
import requests 

def HomePageView(request):
    url = 'http://hapi.fhir.org/baseR4/CarePlan/49011'
    response = requests.get(url)
    db = response.json()
    print(db)
    return render(request , "home.html" , {'db': db})
    
def CreatePageView(request):
    return render(request , 'create_data.html')

 
def EditPageView(request):
    return render(request , "edit_data.html")
 
        
def DeletePageView(request):
    return render(request , 'delete_data.html')
