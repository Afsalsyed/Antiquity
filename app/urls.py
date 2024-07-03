from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('product/<int:pk>/', views.details, name="details"),
    path('post-product/', views.post_product, name='post-product'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('my-listings/', views.my_listings, name='my-listings'),
]

