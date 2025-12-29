from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shop/", include("shop.urls")),
]

if settings.DEBUG:
    static_dir = BASE_DIR / "static"
    urlpatterns += static(settings.STATIC_URL, document_root=static_dir)
