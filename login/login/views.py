from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response
from django.contrib.auth import login as django_login
from django.contrib.auth.models import User
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

    user=jsonobj.get('user')
    username = jsonobj.get('username')
    mob_no = jsonobj.get('mob_no')
    email = jsonobj.get('email')
    password = jsonobj.get('password')

    print username,mob_no,email,password


    user = User.objects.create(username=user)
    user.set_password(password)
    user.save()
    # user_detail =UserDetail.objects.all()
    # print user_detail.email



    user_reg = UserLoginForm.objects.create(username=username,mob_no=mob_no,email=email,user=user)
    user_reg.save()

    # return HttpResponse(json.dumps({"validation":"employee added succesfully","status":True}), content_type="application/json")
    return render_to_response('html_templates/home.html')



def loginme(request):
    # jsonobj=json.loads(request.body)

    jsonobj = request.POST
    # print jsonobj

    username=jsonobj.get("username")
    password=jsonobj.get("password")


    if username is None:
        return HttpResponse(json.dumps({'validation':'Enter user name' , "status": False}), content_type="application/json")
    elif password is None:
        return HttpResponse(json.dumps({'validation':'Enter password first' , "status": False}), content_type="application/json")

    
    # if  not username.__contains__('@') or  len(username) <= 10:
    #     return HttpResponse(json.dumps({'validation':  'please enter valid username' , "status": False}), content_type="application/json")
    # else:
    user_detail = UserLoginForm.objects.all()
    for user__ in user_detail:
        print '----------------------------------------------'
        print '@@@@@@ email' ,user__.email 
        print '%%%%%% mob_no' , type(user__.mob_no)
        print '###### username' , type(user__.username)

        print username


        
        if str(user__.mob_no) == username or user__.email == username:
            user_st = user__.username
            user=  authenticate(username=user_st,password=password)
            print user.id
            
            if not user:
                  return HttpResponse(json.dumps({'validation':'Invalid user', "status": False}), content_type="application/json")
            if not user.is_active:
                  return HttpResponse(json.dumps({'validation':'The password is valid, but the account has been disabled!', "status":False}), content_type="application/json")

            django_login(request,user)
    queryset = show_user(user)
    return render_to_response('html_templates/show_user.html',queryset)

    # if not user:
    #     return HttpResponse(json.dumps({'validation':'Invalid user', "status": False}), content_type="application/json")
    # if not user.is_active:
    #     return HttpResponse(json.dumps({'validation':'The password is valid, but the account has been disabled!', "status":False}), content_type="application/json")

    # queryset = show_user(user)
    # return render_to_response('html_templates/show_user.html',queryset)
    # django_login(request,user)
    # return HttpResponse(json.dumps({'validation':'Login successfully', "status": True}), content_type="application/json")




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

