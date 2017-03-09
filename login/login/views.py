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

    print username,mob_no,email,password

    
    user_reg = UserLoginForm.objects.create(username=username,mob_no=mob_no,email=email,password=password)
    user_reg.save()

    return render_to_response('html_templates/home.htm l')



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


    # user = UserLoginForm.objects.get(username=username,password=password)
    # user = authenticate(username=username,password=password)
    user_detail = UserLoginForm.objects.all()
    print user_detail

    for user in user_detail:
        print user
        if username == user.username or username == user.email:
            queryset = show_user(user)
            return render_to_response('html_templates/show_user.html',queryset)
    return HttpResponse(json.dumps({'validation':'Invalid user', "status": False}), content_type="application/json")



    # if not user:
    #     return HttpResponse(json.dumps({'validation':'Invalid user', "status": False}), content_type="application/json")
    # else:
    #     queryset = show_user(user)
    #     return render_to_response('html_templates/show_user.html',queryset)


def show_user(user):

    user_info = UserLoginForm.objects.get(username=user)

    username = user_info.username
    email = user_info.email
    mob_no =user_info.mob_no

    queryset = { "user":username,
                    "email":email,
                        "mob_no":mob_no
            }

    return queryset

