from django import template
import re

register = template.Library()

CENSORED_WORDS = ['редиска', 'дурак', 'идиот', 'скуф', 'скуфяра']  # список нежелательных слов

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Фильтр 'censor' можно применить только к строкам.")

    def replace_word(match):
        word = match.group()
        return word[0] + '*' * (len(word) - 1)

    pattern = r'\b(' + '|'.join(re.escape(word) for word in CENSORED_WORDS) + r')\b'
    pattern = re.compile(pattern, flags=re.IGNORECASE)

    return pattern.sub(replace_word, value)