from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    # temp = User.objects.all()
    # for usr in temp:
    #     print("Username {}, Email {}".format(usr.username, usr.email))
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid(): # clean method is called when i am calling form.is_valid where i check whether email already exists or not
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for %s!"%username)
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    #print("USERRRR{}".format(type(request.user)))
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST ,
                                    request.FILES,
                                    instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "details updated successfully!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)
