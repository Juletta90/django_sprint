from django.shortcuts import render


def about(request):
    """Страница 'О проекте'."""
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request):
    """Страница 'Наши правила'."""
    template_name = 'pages/rules.html'
    return render(request, template_name)


# https://nuancesprog.ru/p/13061/

