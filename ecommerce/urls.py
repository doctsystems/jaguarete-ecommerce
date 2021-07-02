from django.contrib import admin
from django.urls import path, include

# For static and media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include(('store.urls', 'store'), namespace='store')),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/', include(('users.urls', 'users'), namespace='users')),
  path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
  path('orders/', include(('order.urls', 'order'), namespace='order')),
  path('productos/', include(('producto.urls', 'producto'), namespace='producto')),
]

# static and media Urls
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
