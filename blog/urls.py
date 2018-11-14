from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
#from .models import Post, Category


app_name="blog"
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.main, name='main'),
	path('articles/', views.article_list, name='article_list'),
	path('article/detail/<int:article_id>', views.article_detail, name='article_detail'),

    # re_path(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
