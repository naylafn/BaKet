from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('feeds/', include('apps.feeds.urls')),
    path('articles/', include('apps.articles.urls')),
    path('catalogue/', include('apps.catalogue.urls')),
    path('wishlist/', include('apps.wishlist.urls')),
    path('user/', include('apps.user.urls'))
]

urlpatterns += staticfiles_urlpatterns()