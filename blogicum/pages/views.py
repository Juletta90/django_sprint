from django.shortcuts import render


# view-функция возвращает функцию render(), в которую передаётся
# объект запроса request и адрес HTML-шаблона
def about(request):
    """Страница 'О проекте'."""
    # адрес шаблона отсчитывается от корня папки templates/
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request):
    """Страница 'Наши правила'."""
    template_name = 'pages/rules.html'
    return render(request, template_name)
