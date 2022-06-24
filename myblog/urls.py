
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('um_felagid', views.about, name='about'),
    path('adild', views.adild, name='adild'),
    path('umsagnir', views.blog, name='blog'),
    # path('frettir', views.frettir, name='frettir'),
    path('radgjof', views.radgjof, name='radgjof'),
    path('contact', views.contact, name='contact'),
    path('<str:slug>', views.SingleBlog, name='SingleBlog'),
    #path('contact', views.home, name='home'),





]
