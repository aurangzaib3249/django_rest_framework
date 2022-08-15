from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
   
    path("",HomeView.as_view(),name="home"),
    path("/<str:pk>",HomeView.as_view(),name="home"),
    path('profile/', UserProfiles.as_view(), name='profile'),
    path('Rest-Password/', RestPassword.as_view(), name='profile'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('change-Password/<uid>/<token>/', changePassword.as_view(), name='changePassword'),
    path('changePassword/', ChangePasswordWithOldPassword.as_view(), name='change-Password'),
    
]
