from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('feeds/', include('apps.feeds.urls')),
    path('articles/', include('apps.articles.urls')),
    path('catalogue/', include('apps.catalogue.urls')),
    path('wishlist/', include('apps.wishlist.urls')),
    path('user/', include('apps.user.urls'))
]
