from django import template

register = template.Library()


@register.filter
def hide_forbidden(value):
    words = value.split()
    result = []
    forbidden_words = ['fuck', 'fucked', 'fucking', 'nigger', 'niggers', 'whore', 'whores', 'slut', 'sluts',
                       'bitch', 'freak', 'douchebag', 'faggot', 'homo', 'prick', 'dick', 'cunt', 'pussy']
    for word in words:
        if word in forbidden_words:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)
