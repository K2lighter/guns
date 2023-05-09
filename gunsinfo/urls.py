from django.conf.urls.static import static
from django.urls import path, include

from guns import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('pistol', pistol, name='pistol'),
    path('<int:pk>', GunsDetailView.as_view(), name='guns_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = pageNotFound
