from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import eventsapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('blogapp.urls')),
    path('', eventsapp.views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
