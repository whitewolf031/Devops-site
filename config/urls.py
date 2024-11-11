from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from ownsite.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drf-auth/', include('rest_framework.urls')),  # SessionAuthentication

    path('contact/create/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/', DevopsRetrive.as_view(), name='contact-retrieve'),
    path('contact/delete/<int:pk>/', DevopsDestroy.as_view(), name='contact-destroy'),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
