from django.shortcuts import render
from .forms import LoginForm, RegisterForm, UserEditForm, ProfileEditForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
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

# User Dashboard
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})

# User Register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # Save Password in Database
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                new_user = form.save(commit=False)
                new_user.set_password(
                    form.cleaned_data['password']
                )
                new_user.save()
                Profile.objects.create(user=new_user)
                return render(request, 'accounts/register_done.html', {'new_user':new_user})
    
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

# User Register
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # User Messages
            messages.success(request, 'Good it was successfully!')
        else:
            messages.error(request, 'An Error is Happend!')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'accounts/edit.html', {'user_form':user_form, 'profile_form':profile_form} )