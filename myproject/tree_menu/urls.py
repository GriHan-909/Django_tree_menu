from django.urls import path
from django.http import HttpResponse
from .views import home_view

def stub_view(request):
    return HttpResponse("Заглушка страницы")

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', stub_view),
    path('about/team/', stub_view),
    path('about/history/', stub_view),
    path('services/', stub_view),
    path('services/dev/', stub_view),
    path('services/dev/django/', stub_view),
    path('services/design/', stub_view),
    path('contact/', stub_view),
]
