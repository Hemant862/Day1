from django.shortcuts import render,redirect
from . models import Student
from django.views import View


class AddView(View):
    def get(self,request):
        template_name = "addstu.html"
        context = {}
        return render(request, template_name, context)

    def post(self,request):

            n = request.POST['name']
            rn = request.POST["rollno"]
            m = request.POST["marks"]
            s = Student(name=n, rollno=rn, marks=m)
            s.save()
            return redirect("/student/show/")



# def addview(request):
#     if request.method=="POST":
#         n=request.POST['name']
#         rn=request.POST["rollno"]
#         m=request.POST["marks"]
#         s=Student(name=n,rollno=rn,marks=m)
#         s.save()
#     template_name="addstu.html"
#     context={}
#     return render(request, template_name, context)

def showView(request):
    student=Student.objects.all()
    template_name="showstu.html"
    context={"student":student}
    return render(request, template_name, context)


class UpdateView(View):

    def get(self,request,i):
        s=Student.objects.get(id=i)
        template_name = "addstu.html"
        context = {"s": s}
        return render(request, template_name, context)

    def post(self,request,i):
        s = Student.objects.get(id=i)
        n = request.POST["name"]
        rn = request.POST["rollno"]
        m = request.POST["marks"]
        s.name = n
        s.rollno = rn
        s.marks = m
        s.save()
        return redirect("/student/show/")


# def updateView(request,i):
#     s=Student.objects.get(id=i)
#     if request.method=="POST":
#         n=request.POST["name"]
#         rn=request.POST["rollno"]
#         m = request.POST["marks"]
#         s.name=n
#         s.rollno=rn
#         s.marks=m
#         s.save()
#     template_name = "addstu.html"
#     context = {"s":s}
#     return render(request, template_name, context)

def deleteView(request,i):
    s=Student.objects.get(id=i)
    if request.method== "POST":
        s.delete()

        return redirect("/student/show/")
    context={"s":s}
    template_name="deletestu.html"
    return render(request, template_name, context)






