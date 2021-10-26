from django.urls import path
from . import views
from .views import addprofile


urlpatterns = [
    path('', views.home, name="home"),
    path('membership', views.membership, name="membership"),
    path('contact', views.contact, name="contact"),
    path('partner', views.partnersearch, name="partner"),
    path('search_id', views.searchbyID, name="search_id"),
    path('about', views.about, name="about"),
    path('payment', views.payment, name="payment"),
    path('search', views.search, name="search"),
    path('add_profile', views.addprofile, name="add_profile"),
]
