from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout


def loginView(request):
    if request.method=="POST":
        u=request.POST.get("uname")
        p=request.POST.get("pw")
        user= authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect("/student/show/")
    template_name= "AUTHAPP/login.html"
    context = {}
    return render(request, template_name, context)

def registerView(request):
    form= UserCreationForm()
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/auth/login/")
    template_name="AUTHAPP/register.html"
    context={"form":form}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect("/auth/login/")

# Create your views here.
