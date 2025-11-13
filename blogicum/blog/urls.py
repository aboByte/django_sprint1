from django.urls import path
from . import views

ctposts = views.category_posts
app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:id>/", views.post_detail, name="post_detail"),
    path("category/<slug:category_slug>/", ctposts, name="category_posts"),
]
