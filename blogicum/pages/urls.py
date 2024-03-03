from django.urls import path
from . import views


# Указываем namespace для ссылок приложения
app_name: str = 'pages'

# Имя шаблона такое же, как у функции
urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
