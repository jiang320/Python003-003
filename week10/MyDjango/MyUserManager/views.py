from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse
from django.contrib.auth import login,logout,authenticate

# Create your views here.
#from django.urls import reverse
from django.views import View
from django.views.generic import View


def index(request):
    return HttpResponse("Hello Django!,please login")

class Regist(View):
    TEMPLATE = 'regist.html'

    def get(self,request):
        if request.user.is_authenticated:
            return  redirect(reverse('login'))

        # error = request.Get.get('error','')
        error = request.GET.get('error','')
        #django AttributeError: 'WSGIRequest' object has no attribute 'Get'

        return render(request,self.TEMPLATE,{'error':error})

    def post(self,request):
        username = request.POST.get('username')
        password =request.POST.get('password')
        check_password = request.POST.get('check_password')

        if password != check_password:
            return  redirect('/regist?error=user not exist ')
        exists =User.objects.filter(username=username).exists()

        if exists:
            return redirect('/regist?error= has exists')

        user =User.objects.create_user(
            username=username,
            password=password
        )
        user.save()
        return redirect(reverse('login'))


class Login(View):

    TEMPLATE='login.html'

    def get(self, request):
        error=request.GET.get('error','')
        return render(request,self.TEMPLATE,{'error':error})


    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        exists =User.objects.filter(username=username).exists()

        if not exists:
            return  redirect('/login?error=没有该用户')

        user =authenticate(username=username,password=password)

        if user:
            login(request,user)
        else:
            return redirect('/login?error=wrong password')
        return  redirect('/login')
#



class LogoutUser(View):

    def get(self, request):
        logout(request)
        return  redirect(reverse('login'))














