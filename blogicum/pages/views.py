from django.shortcuts import render


def about(request):
    """Страница 'О проекте'."""
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request):
    """Страница 'Наши правила'."""
    template_name = 'pages/rules.html'
    return render(request, template_name)


#def page_not_found(request, exception):
#    return render(request, "pages/404.html", status=404)


# https://nuancesprog.ru/p/13061/



#
# # def pageNotFound(request, exception):
# #     return HttpResponseNotFound('<h1>Страница не найдена</h1>')