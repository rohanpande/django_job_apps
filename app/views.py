from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
import traceback

from app.models import JobPost

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First Job Description",
    "Second Job Description",
    "Third Job Description"
]

# # Create your views here.
# def hello(request):
#     return HttpResponse("<h3>Hello World!!!.<h3>")

class TempClass:
    x = 5

def hello(request):

    temp = TempClass()
    is_authenticated = False
    list = ["alpha", "beta"]
    context = {"name": "Django", "age": 30, "first_list": list,
               "temp_object": temp, 'is_authenticated': is_authenticated}
    
    return render(request, "apps/hello.html", context)

# Create Job Details
def job_detail(request, job_id):

    try:
        if job_id == 0:
            return redirect(reverse('jobs_home'))
        job = JobPost.objects.get(id=job_id)
        context = {'job':job}
        return render(request, "apps/jobs_detail.html", context)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return HttpResponseNotFound('Not Found')

def job_list(request):

    jobs = JobPost.objects.all()
    context = {'job_title_list': jobs}
    
    return render(request, "apps/index.html", context)