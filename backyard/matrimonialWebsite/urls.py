"""matrimonialWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

api_urls = [
    path('v1/', include('human.urls')),

    path('', include('djoser.urls')),

    # JWT Authentication
    path('jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns = [
    path('api/', include(api_urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('api/auth/', include('rest_framework.urls'))
    ] + urlpatterns

# Admin Site Config
admin.sites.AdminSite.site_header = 'Matrimonial Website'
admin.sites.AdminSite.site_title = 'Welcome to admin area of '+str(admin.sites.AdminSite.site_header)
admin.sites.AdminSite.index_title = admin.sites.AdminSite.site_title
