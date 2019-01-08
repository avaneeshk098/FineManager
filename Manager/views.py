from django.shortcuts import render
from .forms import FineForm, RegisterForm
from .models import Fine,EmployeeUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
@login_required
def add_fine(request):
    if request.method == "POST":
        form = FineForm(request.POST)
        if form.is_valid():
            for i in EmployeeUser.objects.values():
                name = request.POST.get("employee").split(" ")
                name1 = i["name"].split(" ")
                if name1[0] == name[0] and name1[-1] == name[-1] or i["employee_id"] == request.POST.get("employee_id"):
                    post = form.save(commit = False)
                    post.save()
                    return redirect('/manager/home/', pk=post.pk)
                else:
                    return HttpResponse("Invalid Employee")
    else:
        form = FineForm()
    return render(request, 'add_fine.html', {'form':form})


@login_required
def view_fine(request):
    context = Fine.objects.all()
    sum = 0
    if request.method == "GET":
        employe = request.GET.get("search")
        try:
            for i in context:                   
                context = Fine.objects.filter(employee__contains=employe).values("employee_id","employee","fine","reason","date_applied")
                    
        except ValueError:
            print("Not Valid Search")
            
    for i in context.values():
        sum += i['fine']
            
    return render(request, "view_fine.html", {'db':context,
                                                  'employee':list,
                                                  'sum':sum})

def delete_fine(request):
    context = Fine.objects.all()
    if request.method == "GET":
        employe = request.GET.get("search")
        try:
            for i in context:               
                context = Fine.objects.filter(employee__contains=employe).values("id","employee","fine","reason","date_applied")
        except ValueError:
            print("Not Valid Search")
        delete_id = request.GET.get("ID")
        Fine.objects.filter(pk = delete_id).delete()    
    return render(request, "delete_fines.html", {'db':context,
                                                 'id':delete_id})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegisterForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/manager/')
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = RegisterForm()
    return render(request,'reg.html',
                          {'user_form':user_form,
                           'registered':registered})
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/manager/home/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user_login.html', {})

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect("/manager/")


def employee_register(request):
    registered = False
    if request.method == 'POST':
        employee = EmployeeUser()
        user_form = RegisterForm(data=request.POST)
        if user_form.is_valid():
            employee_id = request.POST.get('username')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            employee.employee_id = employee_id
            employee.password = password
            employee.name = first_name + " " + last_name
            employee.save()
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/')
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = RegisterForm()
    return render(request,'employee_register.html',
                          {'user_form':user_form,
                           'registered':registered})
        
def employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('employee_id')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'employee_login.html', {})
    
@login_required
def employee_view(request):
    sum = 0
    name = request.user.first_name + " " + request.user.last_name
    username = request.user.username
    context1 = Fine.objects.filter(employee_id__contains=username).values("employee_id","employee","fine","reason","date_applied")
    context2 = Fine.objects.filter(employee__contains=name).values("employee_id","employee","fine","reason","date_applied")
    context = context1 | context2
    values = Fine.objects.values("fine")
    for i in context:
        sum += i['fine']
    
    return render(request, "employee_view.html", {'db':context,
                                                  'sum':sum})
    
@login_required
def manager_employee_view(request):
    context = EmployeeUser.objects.all()  
    if request.method == "GET":
        employe = request.GET.get("search")
        try:
            for i in context:               
                context = EmployeeUser.objects.filter(name__contains=employe).values("employee_id","name")
                    
        except ValueError:
            print("Not Valid Search")
    return render(request, "manager_employee_view.html", {'db':context})
    