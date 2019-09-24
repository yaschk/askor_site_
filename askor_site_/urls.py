from django.contrib import admin
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from askor import views
from django.conf.urls.i18n import i18n_patterns
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('currencies/', include('currencies.urls')),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('contacts/', views.contacs, name='contacts'),
    path('category/<product_category>/', views.product_catalog, name='product_catalog'),
    path('category-table/<product_category>/', views.product_table, name='product_table'),
    path('category/<product_category>/product/<product_id>/', views.product, name='product'),
)
