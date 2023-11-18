from django.urls import path, re_path
from . import views

intorfloat_re = "(\d+(?:\.\d+)?)"

urlpatterns = [
    path('sdata/', views.sdata),
    path('tdata/', views.tdata),
    path('dash/',views.dash),
    # re_path(r'dash/', views.dash)
    re_path(r'^dash/(?P<cn>\w+?)/$', views.dash),
    re_path(r'^dash/(?P<cn>\w+?)/(?P<clat>\w+?)/(?P<clon>\w+?)/$', views.dash),
    re_path(r'^dash/<str:cn>/<float:clat>/<float:clon>/$',views.dash),
    re_path(r'^dash/(P<cn>\d+)/(P<clat>\d+)/(P<clon>\d+)/$',views.dash),
    re_path(r'^dash/(P<str:cn>\d+)/[0-9]+\.?[0-9]/[0-9]+\.?[0-9]+$', views.dash),
    path('^dash/<str:cn>/'+intorfloat_re+"/"+intorfloat_re, views.dash),
    path(r'^dash/$', views.dash)
]
