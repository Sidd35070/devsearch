from django.contrib import admin
from django.urls import path, include
from django.conf import settings, settings
from django.conf.urls.static import static

from projects.views import projects

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls') )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
