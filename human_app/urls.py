from . import views
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
    path('skintone.html',views.skintone,name='skintone'),
    path('about.html',views.about,name='about'),
    path('SaveImage',views.SaveImage , name='SaveImage'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)