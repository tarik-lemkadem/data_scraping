from django.shortcuts import render
from django.http import HttpResponse
from scraping.models import Job
from django.core import management



# Create your views here.
def home(request):
    return render(request,'home.html')



def job(request):
    
    job_obj = Job.objects.all()
    if request.method == 'POST' and 'scrape' in request.POST:

        management.call_command( "scrape" )

    

    # return user to required page
       

    
    context = {
        
        "job" : job_obj,

    }

    return render(request, "job.html", context)