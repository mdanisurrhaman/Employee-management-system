from django.shortcuts import render,redirect
from django.http import HttpResponse
from test_app.models import *
from test_app.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return HttpResponse("welcome django class")


def index(request):
   data={
       'info':[{'name':'abc','age':21},
               {'name':'xyz','age':20},
               {'name':'def','age':19}],
       'products':['dryfruits','spices','rice']
   }
   return render(request , 'index.html', data) 
@login_required
def getdata(request):
    employee=Employee.objects.all
    department=Department.objects.all()
    return render(request, 'index.html' , context={'emp':employee, 'dep': department})


def about(request):
    return render(request,'about.html')

def addData(request,):
    if request.method=='POST':
        name=request.POST['name']
        department=request.POST['department']
        salary=request.POST['salary']
        age=request.POST['age']
        Employee.objects.create(name=name,department=department,salary=salary,age=age)
        return redirect('getdata')



    return render(request,'add_data.html')


def updateData(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        employee.name=request.POST['name']
        employee.department=request.POST['department']
        employee.salary=request.POST['salary']
        employee.age=request.POST['age']
        employee.save()
        return redirect('getdata')
    return render(request,'update.html',context={'emp':employee})


def Delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('getdata')


# --------------------------Student Crud-----------------------------------------

def Students(request):
     student=Student.objects.all
     return render(request, 'student.html' , context={'Student':student})



def Addstudent(request):
    if request.method=='POST':
        name=request.POST['name']
        roll_no=request.POST['roll_no']
        semester=request.POST['semester']
        # branch=request.POST['branch']
        phone_no=request.POST['phone_no']
        Student.objects.create(name=name,roll_no=roll_no,semester=semester, phone_no=phone_no)
        return redirect('Students')
    return render(request,'addstudent.html')



def updatestudent(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        student.name=request.POST['name']
        student.roll_no=request.POST['roll_no']
        student.semester=request.POST['semester']
        # student.branch=request.POST['branch']
        student.phone_no=request.POST['phone_no']
        student.save()
        return redirect('Students')
    return render(request,'updatestudent.html',context={'student':student})


def deletes(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('Students')


# ----------------------------contact-----------------------
def contact(request):
    form=Contactform()
    if request.method=='POST':
        
        form=Contactform(request.POST)
        form.save()
        return redirect('Students')
    return render(request,'contact.html', context={'f':form})


# ----------------------user Register---------------------
def register(request):
    rform=UserCreationForm()
    if request.method=='POST':
     rform=UserCreationForm(request.POST)
     if rform.is_valid():
         rform.save()
         return redirect('getdata')

    return render(request,'userregisteration.html', context={'f':rform})
    

def login_view(request):
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('getdata')

        return render(request,'login.html')
    


def logout_view(request):
    logout(request)
    return redirect('login')    

