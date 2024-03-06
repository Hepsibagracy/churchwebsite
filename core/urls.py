from django.urls import path
from core import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('watch/',views.watch,name='watch'),
    path('prayer/',views.prayer,name='prayer'),
    path('contact/',views.contact,name='contact'),
    path('location/',views.location,name='location')
]