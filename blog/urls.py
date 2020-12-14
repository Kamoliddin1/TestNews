from django.urls import path

from .views import IndexView, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create_news/', NewsCreateView.as_view(), name='create_news'),
    path('update_news/<int:pk>', NewsUpdateView.as_view(), name='update_news'),
    path('delete_news/<int:pk>', NewsDeleteView.as_view(), name='delete_news'),
]
