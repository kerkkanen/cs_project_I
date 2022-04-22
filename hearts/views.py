from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .models import User
from .models import Account
from .models import Message


@login_required
def index(request):
    user = request.user
    if user.username == 'admin':
        return render(request, 'hearts/index.html')
    account = Account.objects.get(owner=user.id)
    messages = Message.objects.all()
    searched = ""
    try:
        searched = request.session['person']
    except KeyError:
        request.session['person'] = None
    return render(request, 'hearts/index.html', {'account': account, 'person': searched, 'messages': messages})


def logout(request):
    django_logout(request)
    return redirect('index')


def find(request):
    if request.method == "POST":
        searched = request.POST.get('searched')        
        query = "SELECT * FROM auth_user WHERE username = '%s';" % searched
        user = User.objects.raw(query)        
        if len(user) > 0:
            name = str(user[0])
            request.session['person'] = name
    return redirect('index')


def transfer(request):
    if request.method == "POST":
        sender = request.user
        to = request.session['person']
        amount = int((request.POST.get('amount')))
        receiver = User.objects.get(username=to)
        send(sender, receiver, amount)
        content = str(request.POST.get('message'))
        Message.objects.create(
            sender=sender, receiver=receiver, content=content)
    return redirect('index')


def send(sender, receiver, amount):
    sender_a = Account.objects.get(owner=sender)
    receiver_a = Account.objects.get(owner=receiver)

    sender_a.hearts -= amount
    receiver_a.hearts += amount

    sender_a.save()
    receiver_a.save()
    return


def delete(request):    
    return HttpResponse("Anyone could delete anything here!")

def change(request):
    if request.method == "POST":
        user = request.user
        user = User.objects.get(username=user.username)
        password = request.POST.get('new')
        user.set_password(password)
        user.save()
    return redirect('index')
