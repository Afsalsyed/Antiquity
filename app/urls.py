from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("details", views.details, name="details"),
    path('post-product/', views.post_product, name='post-product'),
]

