# # views.py
# from django.contrib.auth import login, logout
# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views import View
# from django.views.generic.edit import CreateView
# from .forms import CustomUserCreationForm, CustomAuthenticationForm


from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# from .models import CustomUser

# def index(request):
#     return render(request, 'registration/index.html')

# @api_view(['GET'])
# def check_user_active(request, username):
#     try:
#         user = CustomUser.objects.get(username=username)
#     except CustomUser.DoesNotExist:
#         raise Http404("User not found")

#     data = {
#         'username': user.username,
#         'is_active': user.is_active,
#     }

#     return Response(data, status=status.HTTP_200_OK)


# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')

# class LoginView(View):
#     form_class = CustomAuthenticationForm
#     template_name = 'registration/login.html'

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request, data=request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect('home')
#         return render(request, self.template_name, {'form': form})

# class LogoutView(View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('login')



from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from backend.models import CustomUser
from .forms import CustomUserCreationForm

def index(request):
    return render(request, 'backend/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticate(username=user.username, password=user.password)
            if user is not None:
                login(request, user)
                
                return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'backend/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('index')  # Replace 'home' with your desired home URL
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'backend/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('index')  # Redirect to the login page after logout

@api_view(['GET'])
def check_user_active(request, username):
    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        raise Http404("User not found")

    data = {
        'username': user.username,
        'is_active': user.is_active,
    }

    return Response(data, status=status.HTTP_200_OK)
