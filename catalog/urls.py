from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import IndexListView, ContactsListView, ProductDetailView, BlogListView, BlogDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('item_info/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('item_create/', ProductCreateView.as_view(), name='product_create'),
    path('item_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('item_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

    path('contacts/', ContactsListView.as_view(), name='contacts'),

    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_update/<slug:slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<slug:slug>/', BlogDeleteView.as_view(), name='blog_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
