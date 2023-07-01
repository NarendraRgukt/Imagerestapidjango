
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from imageapp.views import ImageViewSet,UserLoginapiView
router=DefaultRouter()
router.register('image',ImageViewSet)

urlpatterns = [
    path("",include(router.urls)),
    path('login/',UserLoginapiView.as_view(),name="loginauth")

    
]
