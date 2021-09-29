from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values for "arg" from the string !

    """

    return value.replace(arg, '')

    #register.filter('cut', cut)
    #we  comment this to use a decorator as above
