from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^yakima/', include('yakima.urls')),
    url(r'^admin/', admin.site.urls),
]
