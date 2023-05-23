from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    '''logout user'''
    logout(request)
    return HttpResponseRedirect(reverse('stockright:index'))

def register(request):
    '''Register a new user'''
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #Login the user and redirect to homepage
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('stockright:index'))
    context = {'form':form}
    return render(request, 'users/register.html', context)
