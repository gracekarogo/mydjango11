from django.shortcuts import render, redirect
from hospitalapp.models import Member, Contacts, Users

# Create your views here.
def index(request):
    if request.method == 'POST':
       contact = Contacts(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'], message=request.POST['message'])
       contact.save()
       return redirect('/')
    else:
       return render(request, 'index.html')

def inner(request):
    return render(request, 'inner-page.html')

def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST["username"],email=request.POST['email'],password=request.POST['password'])
        member.save()
        return redirect('/register')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'Login.html')

def upload(request):
    return render(request, 'Upload.html')

def details(request):
    details = Contacts.objects.all()
    return render(request, 'details.html')

def users(request):
    users = Users.objects.all()
    return render(request, 'users.html',{'users':users})