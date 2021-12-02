from django.contrib import admin
# from baton.autodiscover import admin
from django.urls import path, include


api = [
    path('', include('mainAPI.urls')),
    path('register/', include('register.urls'))
]


urlpatterns = [
    path('api/', include(api)),
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),

]
