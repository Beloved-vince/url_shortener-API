from django.urls import path
from .views import URLShortenerCreate, URLShortenerRetrieveUpdateDelete, ClickCreate

urlpatterns = [
    path('urls/', URLShortenerCreate.as_view(), name='url_shortener_create'),
    path('urls/<str:short_url>/', URLShortenerRetrieveUpdateDelete.as_view()),
    path('urls/<str:short_url>/click/', ClickCreate.as_view()),
]
