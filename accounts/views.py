from django.contrib.auth import authenticate, login, logout
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
