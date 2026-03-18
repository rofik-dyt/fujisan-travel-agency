from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('packages/', views.packages_view, name='packages'),
    path('blog/', views.blog_list_view, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail_view, name='blog_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
]
