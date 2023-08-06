from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts, item_info

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('item_info/<int:pk>/', item_info)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
