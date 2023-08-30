"""
URL configuration for you_and_meme_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers
from you_and_meme_backend_app.views import ProfileViewSet, PostViewSet, CommentViewSet, MemeViewSet
from rest_framework_simplejwt import views as jwt_views
from you_and_meme_backend_app import views

router = routers.DefaultRouter()
router.register('users', ProfileViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('memes', MemeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    # path('api/token/', CustomTokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
    # path('api/token/refresh/', CustomTokenRefreshView.as_view(),
    #      name='token_refresh'),
    path('user/login/', views.LoginView.as_view(), name="auth-login"),
    path('user/signup/', views.RegisterUsersView.as_view(), name="user-signup"),
]
