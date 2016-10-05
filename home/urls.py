from django.conf.urls import url

from . import views

urlpatterns = [
     url(r'^$', views.home, name='home'),
     url(r'^faq/$', views.faq, name='faq'),
     url(r'^image_gallery/$', views.image_gallery, name='image_gallery'),

]