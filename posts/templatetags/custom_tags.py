from django import template

register = template.Library()


# D4 чтобы пагинация и фильтрация работали вместе
@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()        # кодируем параметры в формат, который может быть указан в строке браузера
