from django.urls import path  # Assurez-vous d'importer 'path' depuis 'django.urls'
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Pages
    path('', views.index, name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
