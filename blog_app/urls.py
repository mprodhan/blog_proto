from django.urls import path
from blog_app import views

urlpatterns = [
    path('signup/', views.signupview, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),

    path('', views.index, name='homepage'),
    path('blog/', views.bloginsert, name='blog'),
    path('author/<int:id>/', views.author_detail, name='author')
]