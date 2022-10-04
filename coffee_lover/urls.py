
from ast import NameConstant
from django.contrib import admin
from django.urls import path, include
from pages import urls
from coffeehouse import urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('coffeehouse/', include('coffeehouse.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
