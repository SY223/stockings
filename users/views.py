from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import LoginForm, UserRegistrationForm


# class MyLoginView(LoginView):
#     redirect_authenticated_user = True
#     template_name='registration/login.html'

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect(reverse('stockright:index'))
#                 else:
#                     return HttpResponse('Disabled Account')
#             else:
#                 return HttpResponse('Invalid Login')
#     else:
#         form = LoginForm()
#         context = {'form':form}
#         return render(request, 'users/login.html', context)
            




# def logout_view(request):
#     '''logout user'''
#     logout(request)
#     return HttpResponseRedirect(reverse('stockright:index'))



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect('registration/register_done.html', args=new_user)
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})
    