# from django.urls import path
# from PMKAPP import views

# urlpatterns = [
#       path('home/', views.home, name='home'),
# ]

from django.urls import path
from PMKAPP import views

urlpatterns = [
    # Landing Page
    path('', views.LandingPage.as_view(), name='landingpage'),

    # Home Page
    path('home/', views.HomeView.as_view(), name='home'),

    # Sign In Page
    path('signin/', views.SigninView.as_view(), name='sign_in'),

    # Sign Up Page
    path('signup/', views.SignupView.as_view(), name='sign_up'),

    # Add Page
    path('add/', views.AddView.as_view(), name='add'),

    # Generate Page
    path('generate/', views.GenerateView.as_view(), name='generate'),

    # About Us Page
    path('about/', views.AboutusView.as_view(), name='about_us'),

    # Add more app-specific URL patterns as needed
]