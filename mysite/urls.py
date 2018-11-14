"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.conf.urls import include

urlpatterns += [
    # path(r'catalog/', include('catalog.urls')),
    # path('', include('firstapp.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]

# Добавьте URL соотношения, чтобы перенаправить запросы с корневового URL, на URL приложения 
from django.views.generic import RedirectView
urlpatterns += [
    # path(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
    #path(r'^$', RedirectView.as_view(url='/firstapp/', permanent=True)),
    path(r'^$', RedirectView.as_view(url='/blog/', permanent=True)),
]

# Используйте static() чтобы добавить соотношения для статических файлов
# Только на период разработки
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)