from django.http import HttpResponse
from .models import MyData
import requests

# Create your views here.
def home(request):
    url='https://demo.pathhub.uk/bulkupload/get_organization'  
    res_json = requests.get(url) 
    res = res_json.json()

    for i in res: 
        
        idd=i["id"]
        description=i['description']
        store=MyData.objects.create(myid=idd,description=description)
        store.save()     
     

    return HttpResponse("Data successfully added")
