from django import template

register = template.Library()

@register.filter
def get_val(sequence, index):
    try:
        return sequence[index]
    except (IndexError, TypeError):
        return None

@register.filter
def get_url(value):
    try:
        line_sum=''
        lines = value.split('/')
        for i in lines:
            line_sum+=str(i)
        return line_sum
    except (IndexError, TypeError):
        return None