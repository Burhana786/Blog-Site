from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView
from django.contrib import messages
from .forms import SignupForm,SigninForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.mail import send_mail

# Create your views here.

# class Home(View):
#     def get(self,request):
#         return render(request,"home.html")


# Template Rendering only   

class Home(TemplateView):
    template_name='home.html'   




# class Signup(View):
#     def get(self,request):
#         form1=SignupForm()
#         return render(request,"reg.html",{'form':form1})
#     def post(self,request):
#         form_data=SignupForm(request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"User registered succeessfully")
#             return redirect('home')
#         else:
#             messages.error(request,"Registration failed")
#             return render(request,"reg.html",{"form":form_data})



# VIEW - NEW APPROACH
# Create ==> model,form_class,template_name --> CreateView

class Signup(CreateView):
    model=User
    form_class=SignupForm
    template_name='reg.html'
    success_url=reverse_lazy('home')
    def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            email_id=form_data.cleaned_data.get('email')
            uname=form_data.cleaned_data.get('username')
            pwd=form_data.cleaned_data.get('password1')
            msg="You are Registered in BlogApp .\n Your Username :"+str(uname)+"\n Password :"+str(pwd)
            form_data.save()
            send_mail(
                'BlogApp Registration',
                msg,
                'djangopro@gmail.com',
                [email_id],
                fail_silently=True
            )
            messages.success(request,"Registration Compleated!!!")
            return redirect('home')
        else:
            messages.error(request,"Registration Failed")
            return render(request,"reg.html",{'form':form_data})




# class SignIn(View):
#     def get(self,request):
#         form1=SigninForm()
#         return render(request,"log.html",{'form':form1})
#     def post(self,request):
#         uname=request.POST.get('username')
#         pw=request.POST.get('password')
#         user=authenticate(request,username=uname,password=pw)
#         if user:
#             print("success")
#             login(request,user)
#             # return HttpResponse("User login success")
#             return redirect('uhome')
#         else:
#             print("failed")
#             # return HttpResponse("User login failed")
#             return redirect("log")



# View a Form ==> form_class,template_name --> FormView

class SignIn(FormView):
    form_class=SigninForm
    template_name='log.html'
    def post(self,request):
        uname=request.POST.get('username')
        pw=request.POST.get('password')
        user=authenticate(request,username=uname,password=pw)
        if user:
            print("success")
            login(request,user)
            # return HttpResponse("User login success")
            return redirect('uhome')
        else:
            print("failed")
            messages.error(request,"Credentials are wrong")
            # return HttpResponse("User login failed")
            return redirect("log")





class SignOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("log")

        