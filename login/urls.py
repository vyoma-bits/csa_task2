from django.urls import path, include
from . import views
urlpatterns = [
    path("login/",views.custlogin,name='custlogin'),
    path("register/",views.custsign,name='custsign'),
    path('social-auth/', include('social_django.urls', namespace='social')),  # Social authentication routes
]
