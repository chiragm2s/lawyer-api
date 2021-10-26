# from django.contrib import admin
# from django.urls import path
# from django.urls.conf import include
# from testapp import views
# from testapp.views import reactView

from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import lawclass

router=DefaultRouter()
router.register('law',lawclass)


urlpatterns = [

  
    path('law/',include(router.urls)),
    #path('test/',views.post),
]
