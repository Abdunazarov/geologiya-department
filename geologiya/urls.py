from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api = [
    path('', include('mainAPI.urls')),
    path('register/', include('register.urls'))
]


urlpatterns = [
    path('api/', include(api)),
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)