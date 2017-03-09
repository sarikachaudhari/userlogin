from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response 
from django.contrib.auth import login as django_login
import json
# Create your views here.

def registration_page(request):
    return render_to_response("html_templates/registration.html")

def login_view(request):
    return render_to_response("html_templates/login.html")

def home_page(request):
    return render_to_response('html_templates/home.html')


def registration(request):
    # jsonobj=json.loads(request.body)
    jsonobj = request.POST
    
    username = jsonobj.get('username')
    mob_no = jsonobj.get('mob_no')
    email = jsonobj.get('email')
    password = jsonobj.get('password')

    login = UserLoginForm.objects.create(username=username,mob_no=mob_no,email=email,password=password)
    login.save()

    return HttpResponse(json.dumps({'validation':"resgistration is successfully",'status':True}), content_type="application/json")




def loginme(request):
    # jsonobj=json.loads(request.body)

    jsonobj = request.POST
    print jsonobj
    
    username=jsonobj.get("username")
    password=jsonobj.get("password")

    if username == None:
        return HttpResponse(json.dumps({'validation':'Enter user name' , "status": False}), content_type="application/json")
    elif password == None:
        return HttpResponse(json.dumps({'validation':'Enter password first' , "status": False}), content_type="application/json")


    user = authenticate(username=username,password=password)
    
    if not user:
        return HttpResponse(json.dumps({'validation':'Invalid user', "status": False}), content_type="application/json")
    if not user.is_active:
        return HttpResponse(json.dumps({'validation':'The password is valid, but the account has been disabled!', "status":False}), content_type="application/json")

    django_login(request,user)
    return HttpResponse(json.dumps({'validation':'user login succefully!', "status":False}), content_type="application/json")


def show_user(request):

    all_user = UserLoginForm.objects.all()

    user_list = []

    for user in all_user:
        user_list.append({"user":user.username,"mob_no":user.mob_no,"email":user.email,"password":user.password})

    user_dict = {}
    user_dict["user_list"] = user_list
    return render_to_response('html_templates/show_user.html',user_dict)

