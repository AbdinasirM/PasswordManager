from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class LandingPage(View):
    def get(self, request):
        # Renders the 'landingpage.html' template for the landing page.
        return render(request, 'PMKAPP/landingpage.html')

class HomeView(View):
    def get(self, request):
        context = {
            'email': 'some@gmail.com',
        }
        # Renders the 'home.html' template for the home page with the 'email' context variable.
        return render(request, 'PMKAPP/home.html', context)

class SigninView(View):
    def get(self, request):
        # Renders the 'sign_in.html' template for the sign-in page.
        return render(request, 'PMKAPP/signin.html')

class SignupView(View):
    def get(self, request):
        # Renders the 'sign_up.html' template for the sign-up page.
        return render(request, 'PMKAPP/signup.html')

class AddView(View):
    def get(self, request):
        # Renders the 'add.html' template for the add page.
        return render(request, 'PMKAPP/add.html')

class GenerateView(View):
    def get(self, request):
        # Renders the 'generate.html' template for the generate page.
        return render(request, 'PMKAPP/generate.html')

class AboutusView(View):
    def get(self, request):
        # Renders the 'about_us.html' template for the about us page.
        return render(request, 'PMKAPP/about_us.html')


class TestView(View):
    def get(self, request):
        # Renders the 'about_us.html' template for the about us page.
        return render(request, 'PMKAPP/test.html')