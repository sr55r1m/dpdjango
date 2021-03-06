"""FDP3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/', views.hello, name='h'),
    path('t/<str:name>/', views.te, name='tep'),
    path('user/<str:na>/<int:roll>/', views.stu),
    path('rw/<str:us>/', views.hy),
    path('hy2/<str:us>/<int:rl>/<int:ag>/', views.hy2),    
    path('register/', views.register,name='register'),  
    path('extcss/', views.extcss,name='extcss'),  
    path('jst/', views.jsac),
    path('jst2/', views.jsac2),  
    path('bot/',views.bot), 
    path('botint/',views.botint),
    path('usrreg/',views.usrrg,name='usrreg'),
    path('usreg/',views.usreg,name='usreg'),
    path('sha/',views.showall,name='sha'),
    path('updt/<int:pe>/',views.update,name='updt'),
    path('udel/<int:pe>/',views.udel,name='udel'),
 
]
