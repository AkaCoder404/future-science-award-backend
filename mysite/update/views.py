from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.handlers.wsgi import WSGIRequest
import datetime

# models
from .models import MyUser, MyUserUploads
from .forms import UploadFile, UploadForm
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the update index")

@csrf_exempt
def upload(request):
    form = UploadFile()
    return render(request, 'myuser/index.html', {'form': form})

def handleFileUpload(request : WSGIRequest):
    print("handle file upload")
    
    # handle other fields
    request_body = request.POST
    name = request_body["name"]
    affiliation = request_body["affiliation"]
    email = request_body["email"]
    category = request_body["category"]
    research = request_body["research"]
    
    # save user for foreignkey
    user = MyUser(name=name, affiliation=affiliation, email=email, category=category, research=research)
    user.save()
    
    # handle files
    print(request.FILES)
    # form = UploadFile(request.POST, request.FILES)
    form = UploadForm(request.POST, request.FILES)
    files = request.FILES.getlist('file')
    print(files)
    if form.is_valid():
        print("form is valid")
        # handle multiple files
        for f in files:
            file_instance = MyUserUploads(file=f, myuser=user, uploadTime = datetime.datetime.now(), filename=f)
            file_instance.save()


    # if form.is_valid():
    #     print("saved")
    #     form.save()

    # send response
    response_data = {}
    response_data['message'] = "Form Successfully Submitted"
    response_data['status'] = 200
    return JsonResponse(response_data)

@csrf_exempt
def update(request : WSGIRequest):
    print(request.content_type)
    print(request.method)
    # if has files, handle upload file method
    if (request.FILES):
        return handleFileUpload(request)
    
    # if normal post request
    if (request.method == "POST"):
        response_data = {}
        response_data['message'] = "message"
        return JsonResponse(response_data)  
    # respond to any other request
    else:
        return HttpResponse("Hello, world. You're at the update index")
