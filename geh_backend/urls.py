
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from post_api.views import CustomConfirmEmailView, CustomLoginView


schema_view = get_schema_view(
    openapi.Info(
        title = 'GeH API',
        default_version= 'v1',
        description= 'API Documentation for GeH backend',
        contact=openapi.Contact(email='gaiusdeveloper@gmail.com'),
    ),
    public= True,
    permission_classes= (permissions.AllowAny,),

)

urlpatterns = [
    path('admin/', admin.site.urls),

    # dj-rest-auth endpoints (login/logout/user)
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('auth/', include('dj_rest_auth.urls')),
    
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/registration/account-confirm-email/<str:key>/',CustomConfirmEmailView.as_view(), name='account_confirm_email'),


    #Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #

    #Products_URL
    path('', include('post_api.urls')),

    ##SWAGGER URLS
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

