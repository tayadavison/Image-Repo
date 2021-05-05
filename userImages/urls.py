from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'images', views.ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('users/<int:pk>/', views.UserDetail.as_view()),
    #path('api-auth/', include('rest_framework.urls'))
]

