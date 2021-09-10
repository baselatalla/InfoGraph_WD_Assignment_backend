from django.urls import path ,include 
from django.conf.urls import url, include
from rest_framework import routers

from .views import MRsListView ,UserViewSet, ImageViewSet, CustomTokenObtainPairView

router = routers.DefaultRouter()
router1 = routers.DefaultRouter()


router.register(r'users', UserViewSet)
router1.register(r'maintenance_requsets', MRsListView)
router1.register(r'images', ImageViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(router1.urls)),
    url(r'^', include(router1.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]