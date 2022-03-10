from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

#User Login View
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
        
#         if form.is_valid():
#             clean_data = form.cleaned_data
#             user = authenticate(request, 
#             username=clean_data['username'], 
#             password=clean_data['password'])

#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse("You are loged in success")
#             else:
#                 return HttpResponse('Your Banned!')
#         else:
#             return HttpResponse('Invalid Login!')
#     else:
#         form = LoginForm()

#     return render(request, 'accounts/login.html', {'form':form})

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})