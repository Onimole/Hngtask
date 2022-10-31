from django.contrib import admin
from django.urls import path, include
from Host_api.views import Info

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', Info.as_view(), name='Host')
]
