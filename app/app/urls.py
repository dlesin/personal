from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('djadmin/', admin.site.urls),
    path('api/', include('backend.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
