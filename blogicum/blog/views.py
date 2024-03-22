from django.shortcuts import render

from django.http import Http404


posts = [
     {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
     },
     {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
     },
     {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
     },
]

# на уровне модуля (т.к. то что расположено на уровне модуля будет просчитано
# только один раз при запуске сервера) собираем новую структуру данных для
# хранения постов (удобнее всего словарь), в которой можно будет за О(1)
# получать нужный пост сразу по его id

# Сделаю сначала словарь формата "id-text" (dict comprehension) генератором словарей
# https://www.sravni.ru/kursy/info/kak-vzyat-znachenie-iz-slovarya-python-i-ne-slomat-prilozhenie/
# https://ru.stackoverflow.com/questions/1427432/%D0%9A%D0%B0%D0%BA-%D0%BD%D0%B0%D0%B9%D1%82%D0%B8-%D0%BD%D1%83%D0%B6%D0%BD%D1%8B%D0%B9-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C-%D0%B5%D1%81%D0%BB%D0%B8-%D0%B5%D1%81%D1%82%D1%8C-value
# https://smartiqa.ru/python-workbook/dict#2

posts_dict = {}
for item in posts:
    posts_dict.update(item)
if not posts_dict:
    raise Http404('Указан неверный id')


def index(request):
    """Вывод записи на главную страницу."""
    sorted_dict = dict(sorted(posts_dict.items()))
    template_name = 'blog/index.html'
    context = {'posts_dict': posts_dict}                   #dict(sorted(posts_dict.items()))}    # {'posts_list': posts[::-1]}
    return render(request, template_name, context)


def post_detail(request, id):
    """Вывод отдельной страницы поста."""
    template_name = 'blog/detail.html'
    context = {'post': posts[id]}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    """Вывод страницы категории."""
    template_name = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template_name, context)
