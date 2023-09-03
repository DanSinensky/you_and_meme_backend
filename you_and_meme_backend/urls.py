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
    path('user/login/', views.LoginView.as_view(), name="auth-login"),
    path('user/signup/', views.RegisterUsersView.as_view(), name="user-signup"),
]
