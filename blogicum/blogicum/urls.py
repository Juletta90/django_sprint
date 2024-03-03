"""blogicum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# название_проекта/urls.py (корневой urls.py проекта)
# Корневой urls.py
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    # Если на сервер пришёл запрос к главной странице,
    # Django проверит на совпадение с запрошенным URL
    # все path() в файле urls.py приложения homepage.
    path('', include('blog.urls', namespace='blog')),
    path('posts/<int:id>/', include('blog.urls', namespace='blog')),
    path(
        'category/<slug:category_slug>/', include('blog.urls', namespace='blog'
                                                  )),
    path('pages/', include('pages.urls', namespace='pages')),
    path('pages/', include('pages.urls', namespace='pages')),
]
