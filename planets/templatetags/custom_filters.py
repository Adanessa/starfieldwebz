from django import template

# Atm this is only for the "fields_to_include" crap. Delete it if you dont need it. Yes I'm talking to you, Mr-put-code-everywhere-and-forget-what-it-do-so-you-cant-remove-it-due-to-fear-of-it-creating-a-black-hole-that-will-end-humanity..

register = template.Library()

@register.filter
def get_attribute(obj, attr_name):
    return getattr(obj, attr_name, '')