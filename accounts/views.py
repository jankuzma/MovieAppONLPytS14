from sqlite3 import IntegrityError

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # autentykacja
        if user is not None:
            login(request, user)  # autoryzacja
            return redirect('index')
        return render(request, 'accounts/login.html')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('index')


class RegisterView(View):

    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            u = User(first_name=first_name, last_name=last_name,username=username)
            u.set_password(password1)
            try:
                u.save()
            except Exception:
                return render(request, 'accounts/register.html', {'msg': 'użytkownik o takiej nazwie już istnieje'})
            login(request, u)
            return redirect('index')
        return render(request, 'accounts/register.html', {'msg':'hasła nie sa takie same'})