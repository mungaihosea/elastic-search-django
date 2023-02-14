from django.urls import path
from .views import BlogPostSearch


urlpatterns = [
    path("", BlogPostSearch.as_view(), name = "search blog post")
]
