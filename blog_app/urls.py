from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog_app import views

urlpatterns = [
    path('signup/', views.signupview, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),

    path('', views.index, name='homepage'),
    path('blog/', views.bloginsert, name='blog'),
    # Check Hyperlink on base.html
    path('author/<str:username>/', views.author_detail, name='author')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )