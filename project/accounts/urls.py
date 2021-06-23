from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from rest_framework_simplejwt.views import TokenObtainPairView


class RestrictOAuthProvidersView(TokenObtainPairView):
    pass



urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/oauth/', RestrictOAuthProvidersView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
