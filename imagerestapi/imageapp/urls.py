
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from imageapp.views import ImageViewSet,CreateUserApiView,CreateUserToken,UserManageApiView
router=DefaultRouter()
router.register('image',ImageViewSet,basename="image")



urlpatterns = [
    path("",include(router.urls)),
    path('create/user',CreateUserApiView.as_view(),name="createuser"),
    path("user/token/",CreateUserToken.as_view(),name="token"),
    path("user/manage/",UserManageApiView.as_view(),name="usermanager")



    
]
