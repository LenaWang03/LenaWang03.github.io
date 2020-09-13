from django.urls import path
from .views import HomePageView, AboutPageView, PaintingsPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), 
    path('', HomePageView.as_view(), name='home'),  
    path('paintings/', PaintingsPageView.as_view(), name='paintings'),
]