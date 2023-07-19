
from django.urls import path,include

from imageapp.views import CreateUserApiView,CreateUserToken,UserManageApiView,ImageViewSet,ItemListCreation
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('image',ImageViewSet,basename="image")







urlpatterns = [
    path('',include(router.urls)),

    path('create/user/',CreateUserApiView.as_view(),name="createuser"),
    path("user/token/",CreateUserToken.as_view(),name="token"),
    path("user/manage/",UserManageApiView.as_view(),name="usermanager"),
    path('image/list/create/',ItemListCreation.as_view(),name="itemlist")




    
]
