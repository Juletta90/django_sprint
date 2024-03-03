# Импортируем функцию path()
# и файл blog/views.py, в котором объявлена view-функция index().

from django.urls import path
from . import views

# Указываем namespace для ссылок приложения/
app_name: str = 'blog'

# Имя шаблона такое же, как у функции
urlpatterns = [
    # Если вызван URL без относительного адреса (шаблон — пустые кавычки),
    # то вызывается view-функция index() из файла views.py
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
]
