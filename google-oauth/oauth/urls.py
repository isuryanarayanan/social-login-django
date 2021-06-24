from django.urls import path
from oauth.views import GoogleOAuthView

urlpatterns = [
    path("google/", GoogleOAuthView.as_view(), name="google-oauth")
]
